import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

#AGENT CLASS
class Agent:
    def __init__(self, name, role, origin, abilities):
        self.name = name
        self.role = role
        self.origin = origin
        self.abilities = abilities

# QUIZ GAME CLASS
class QuizGame:
    def __init__(self, agents):
        self.agents = agents
        self.questions = []
        self.score = 0
        self.current_question = 0

    def generate_questions(self):
        questions = []
        for agent in self.agents:
            questions.append({"question": f"What is {agent.name}'s role?", "answer": agent.role})
            questions.append({"question": f"Which country is {agent.name} from?", "answer": agent.origin})
            ability = random.choice(agent.abilities)
            questions.append({"question": f"Which agent has the ability '{ability}'?", "answer": agent.name})
        random.shuffle(questions)
        self.questions = questions[:10]

    def check_answer(self, answer):
        correct = answer.lower() == self.questions[self.current_question]['answer'].lower()
        if correct:
            self.score += 1
        return correct

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            return self.questions[self.current_question]['question']
        else:
            return None

    def reset(self):
        self.score = 0
        self.current_question = 0
        self.generate_questions()
class QuizGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.player_name = ""

        #LIGHT MODE ALWAYS
        self.bg_color = "#f0f0f0"
        self.fg_color = "#000000"
        self.card_bg = "#ffffff"

        self.root.title("Valorant Agent Quiz")
        self.root.geometry("800x600")
        self.root.config(bg=self.bg_color)

        #Welcome Frame
        self.welcome_frame = tk.Frame(self.root, bg=self.bg_color)
        self.welcome_frame.pack(expand=True)

        tk.Label(self.welcome_frame, text="🎯 Valorant Agent Quiz 🎯", font=("Arial Black", 26),
                 bg=self.bg_color, fg="#FF4655").pack(pady=30)
        tk.Label(self.welcome_frame, text="Enter your player name:", font=("Helvetica", 18),
                 bg=self.bg_color, fg=self.fg_color).pack(pady=10)
        self.name_entry = tk.Entry(self.welcome_frame, font=("Helvetica", 16), width=25)
        self.name_entry.pack(pady=10)

        tk.Button(self.welcome_frame, text="Start Quiz", font=("Helvetica", 16, "bold"), bg="#FF4655",
                  fg="white", activebackground="#FF7F7F", command=self.start_quiz).pack(pady=20)

        #Quiz Frame
        self.quiz_frame = tk.Frame(self.root, bg=self.bg_color)

        #Score and progress
        self.score_label = tk.Label(self.quiz_frame, text="Score: 0 / 10", font=("Helvetica", 16, "bold"),
                                    bg=self.bg_color, fg=self.fg_color)
        self.score_label.pack(pady=10)
        self.progress = ttk.Progressbar(self.quiz_frame, length=600, mode='determinate', maximum=10)
        self.progress.pack(pady=10)

        #Question Card
        self.card = tk.Frame(self.quiz_frame, bg=self.card_bg, bd=5, relief="ridge")
        self.card.pack(pady=20, ipadx=30, ipady=30)

        self.question_label = tk.Label(self.card, text="", font=("Helvetica", 18), wraplength=650,
                                       bg=self.card_bg, fg=self.fg_color)
        self.question_label.pack(pady=20)

        #Multiple-choice buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.card, text="", font=("Helvetica", 14), width=30,
                            command=lambda idx=i: self.submit_answer(idx))
            btn.pack(pady=8)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#FF7F7F"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.card_bg))
            self.option_buttons.append(btn)

    #Start Quiz
    def start_quiz(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        self.player_name = name
        self.game.reset()
        self.welcome_frame.pack_forget()
        self.quiz_frame.pack(expand=True)
        self.show_question()

    #Show Questio
    def show_question(self):
        qdata = self.game.questions[self.game.current_question]
        self.question_label.config(text=f"Q{self.game.current_question + 1}: {qdata['question']}")
        self.score_label.config(text=f"Score: {self.game.score} / 10")
        self.progress['value'] = self.game.current_question

        # Generate random options
        correct = qdata['answer']
        options = [correct]
        while len(options) < 4:
            rand_agent = random.choice(self.game.agents)
            rand_ans = rand_agent.name if "ability" in qdata['question'].lower() else rand_agent.role
            if rand_ans not in options:
                options.append(rand_ans)
        random.shuffle(options)

        for idx, btn in enumerate(self.option_buttons):
            btn.config(text=options[idx], bg=self.card_bg, state="normal")

    #Submit Answer
    def submit_answer(self, idx):
        selected = self.option_buttons[idx].cget("text")
        correct = self.game.check_answer(selected)

        if correct:
            self.option_buttons[idx].config(bg="#4CAF50")
        else:
            self.option_buttons[idx].config(bg="#FF4655")
            for btn in self.option_buttons:
                if btn.cget("text").lower() == self.game.questions[self.game.current_question]['answer'].lower():
                    btn.config(bg="#4CAF50")
        self.root.after(1000, self.next_question)

    #Next Question
    def next_question(self):
        next_q = self.game.next_question()
        if next_q:
            self.show_question()
        else:
            self.end_quiz()

    #End Quiz
    def end_quiz(self):
        score = self.game.score
        message = f"Quiz complete, {self.player_name}!\nYour Score: {score} / 10\n"
        if score >= 8:
            message += "Rank: Valorant Pro"
        elif score >= 5:
            message += "Rank: Agent Trainee"
        else:
            message += "Rank: New Recruit"
        messagebox.showinfo("Quiz Finished", message)
        self.root.destroy()

#AGENTS DATA
agents_data = [
    Agent("Brimstone", "Controller", "USA", ["Incendiary", "Stim Beacon", "Sky Smoke", "Orbital Strike"]),
    Agent("Phoenix", "Duelist", "UK", ["Curveball", "Hot Hands", "Blaze", "Run It Back"]),
    Agent("Sage", "Sentinel", "China", ["Barrier Orb", "Slow Orb", "Healing Orb", "Resurrection"]),
    Agent("Sova", "Initiator", "Russia", ["Owl Drone", "Shock Bolt", "Recon Bolt", "Hunter's Fury"]),
    Agent("Viper", "Controller", "USA", ["Snake Bite", "Poison Cloud", "Toxic Screen", "Viper's Pit"]),
    Agent("Cypher", "Sentinel", "Morocco", ["Trapwire", "Cyber Cage", "Spycam", "Neural Theft"]),
    Agent("Reyna", "Duelist", "Mexico", ["Leer", "Devour", "Dismiss", "Empress"]),
    Agent("Killjoy", "Sentinel", "Germany", ["Alarmbot", "Nanoswarm", "Turret", "Lockdown"]),
    Agent("Breach", "Initiator", "Sweden", ["Aftershock", "Flashpoint", "Fault Line", "Rolling Thunder"]),
    Agent("Omen", "Controller", "Unknown", ["Shrouded Step", "Paranoia", "Dark Cover", "From the Shadows"]),
    Agent("Jett", "Duelist", "South Korea", ["Cloudburst", "Updraft", "Tailwind", "Blade Storm"]),
    Agent("Raze", "Duelist", "Brazil", ["Boom Bot", "Paint Shells", "Blast Pack", "Showstopper"]),
    Agent("Skye", "Initiator", "Australia", ["Regrowth", "Trailblazer", "Guiding Light", "Seekers"]),
    Agent("Yoru", "Duelist", "Japan", ["Fakeout", "Blindside", "Gatecrash", "Dimensional Drift"]),
    Agent("Astra", "Controller", "Ghana", ["Gravity Well", "Nova Pulse", "Nebula", "Astral Form"]),
    Agent("KAY/O", "Initiator", "Unknown (robot)", ["FRAG/ment", "FLASH/drive", "ZERO/point", "NULL/cmd"]),
    Agent("Chamber", "Sentinel", "France", ["Trademark", "Headhunter", "Rendezvous", "Tour De Force"]),
    Agent("Neon", "Duelist", "Philippines", ["Fast Lane", "Relay Bolt", "High Gear", "Overdrive"]),
    Agent("Fade", "Initiator", "Turkey", ["Prowler", "Seize", "Haunt", "Nightfall"]),
    Agent("Harbor", "Controller", "India", ["Cove", "High Tide", "Cascade", "Reckoning"]),
    Agent("Gekko", "Initiator", "USA", ["Dizzy", "Wingman", "Mosh Pit", "Thrash"]),
    Agent("Deadlock", "Sentinel", "Norway", ["GravNet", "Sonic Sensor", "Barrier Mesh", "Annihilation"]),
    Agent("Iso", "Duelist", "China", ["Undercut", "Double Tap", "Kill Contract"]),
    Agent("Clove", "Controller", "Scotland", ["Pick-Me-Up", "Ruse", "Meddle", "Not Dead Yet"])
]


#RUN APP 
if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(agents_data)
    app = QuizGUI(root, game)
    root.mainloop()
