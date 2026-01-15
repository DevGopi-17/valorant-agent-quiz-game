import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import random
import os

# ===== AGENT CLASS =====
class Agent:
    def __init__(self, name, role, origin, abilities, image_path):
        self.name = name
        self.role = role
        self.origin = origin
        self.abilities = abilities
        self.image_path = image_path


# ===== QUIZ GAME CLASS =====
class QuizGame:
    def __init__(self, agents):
        self.agents = agents
        self.questions = []
        self.score = 0
        self.current_question = 0
        self.options = []

    def generate_questions(self):
        questions = []

        for agent in self.agents:
            # Role question
            questions.append({
                "question": f"What is {agent.name}'s role?",
                "answer": agent.role,
                "agent": agent
            })
            # Origin question
            questions.append({
                "question": f"Which country is {agent.name} from?",
                "answer": agent.origin,
                "agent": agent
            })
            # Ability question
            ability = random.choice(agent.abilities)
            questions.append({
                "question": f"Which agent has the ability '{ability}'?",
                "answer": agent.name,
                "agent": agent
            })

        random.shuffle(questions)
        self.questions = questions[:10]

    def next_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.current_question += 1
            return q
        else:
            return None

    def reset(self):
        self.score = 0
        self.current_question = 0
        self.generate_questions()


# ===== GUI CLASS =====
class QuizGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.root.title("Valorant Agent Quiz")
        self.root.geometry("800x600")
        self.root.config(bg="#1E1E1E")  # Dark theme
        self.current_q = None
        self.agent_image_label = None

        # Fonts and colors
        self.title_font = ("Verdana", 20, "bold")
        self.question_font = ("Arial", 16)
        self.button_font = ("Arial", 14)
        self.bg_color = "#1E1E1E"
        self.button_color = "#FF4655"  # Valorant red
        self.button_hover = "#FF7F7F"

        # Welcome frame
        self.welcome_frame = tk.Frame(self.root, bg=self.bg_color)
        self.welcome_frame.pack(pady=50)
        tk.Label(self.welcome_frame, text="Valorant Agent Quiz", font=self.title_font, fg="white", bg=self.bg_color).pack(pady=20)
        tk.Label(self.welcome_frame, text="Enter your player name:", font=self.question_font, fg="white", bg=self.bg_color).pack(pady=10)
        self.name_entry = tk.Entry(self.welcome_frame, font=self.question_font)
        self.name_entry.pack(pady=10)
        tk.Button(self.welcome_frame, text="Start Quiz", font=self.button_font, bg=self.button_color, fg="white", command=self.start_quiz).pack(pady=10)

        # Quiz frame
        self.quiz_frame = tk.Frame(self.root, bg=self.bg_color)

        self.question_label = tk.Label(self.quiz_frame, text="", font=self.question_font, fg="white", bg=self.bg_color, wraplength=700)
        self.question_label.pack(pady=20)

        self.image_canvas = tk.Label(self.quiz_frame, bg=self.bg_color)
        self.image_canvas.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.quiz_frame, text="", font=self.button_font, bg=self.button_color, fg="white",
                            width=25, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.button_hover))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.button_color))
            self.option_buttons.append(btn)

    # ===== QUIZ METHODS =====
    def start_quiz(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        self.player_name = name
        self.game.reset()
        self.welcome_frame.pack_forget()
        self.quiz_frame.pack(pady=20)
        self.show_next_question()

    def show_next_question(self):
        q = self.game.next_question()
        if q is None:
            self.end_quiz()
            return
        self.current_q = q
        self.question_label.config(text=f"Q{self.game.current_question}: {q['question']}")
        self.show_agent_image(q['agent'].image_path)
        self.set_options(q)

    def show_agent_image(self, path):
        if os.path.exists(path):
            img = Image.open(path)
            img = img.resize((200, 200), Image.ANTIALIAS)
            self.imgtk = ImageTk.PhotoImage(img)
            self.image_canvas.config(image=self.imgtk)
        else:
            self.image_canvas.config(image="", text="Image not found", fg="white", font=self.question_font)

    def set_options(self, q):
        # For multiple-choice, pick 3 random wrong options
        answers = [q['answer']]
        while len(answers) < 4:
            a = random.choice(self.game.agents)
            wrong_answer = a.name if "agent" in q and "abilities" in q else (a.role if "role" in q['question'] else a.origin)
            if wrong_answer not in answers:
                answers.append(wrong_answer)
        random.shuffle(answers)
        self.current_q['options'] = answers
        for i, btn in enumerate(self.option_buttons):
            btn.config(text=answers[i])

    def check_answer(self, idx):
        selected = self.current_q['options'][idx]
        correct = self.current_q['answer']
        if selected == correct:
            self.game.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Wrong! Correct answer: {correct}")
        self.show_next_question()

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


# ===== AGENTS DATA WITH IMAGE PATHS =====
agents_data = [
    Agent("Brimstone", "Controller", "USA", ["Incendiary", "Stim Beacon", "Sky Smoke", "Orbital Strike"], "images/Brimstone.jpeg"),
    Agent("Phoenix", "Duelist", "UK", ["Curveball", "Hot Hands", "Blaze", "Run It Back"], "images/Phoenix.jpeg"),
    Agent("Sage", "Sentinel", "China", ["Barrier Orb", "Slow Orb", "Healing Orb", "Resurrection"], "images/Sage.jpeg"),
    Agent("Sova", "Initiator", "Russia", ["Owl Drone", "Shock Bolt", "Recon Bolt", "Hunter's Fury"], "images/Sova.jpeg"),
    Agent("Viper", "Controller", "USA", ["Snake Bite", "Poison Cloud", "Toxic Screen", "Viper's Pit"], "images/Viper.jpeg"),
    Agent("Cypher", "Sentinel", "Morocco", ["Trapwire", "Cyber Cage", "Spycam", "Neural Theft"], "images/Cypher.jpeg"),
    Agent("Reyna", "Duelist", "Mexico", ["Leer", "Devour", "Dismiss", "Empress"], "images/Reyna.jpeg"),
    Agent("Killjoy", "Sentinel", "Germany", ["Alarmbot", "Nanoswarm", "Turret", "Lockdown"], "images/Killjoy.jpeg"),
    Agent("Breach", "Initiator", "Sweden", ["Aftershock", "Flashpoint", "Fault Line", "Rolling Thunder"], "images/Breach.jpeg"),
    Agent("Omen", "Controller", "Unknown", ["Shrouded Step", "Paranoia", "Dark Cover", "From the Shadows"], "images/Omen.jpeg"),
    Agent("Jett", "Duelist", "South Korea", ["Cloudburst", "Updraft", "Tailwind", "Blade Storm"], "images/Jett.jpeg"),
    Agent("Raze", "Duelist", "Brazil", ["Boom Bot", "Paint Shells", "Blast Pack", "Showstopper"], "images/Raze.jpeg"),
    Agent("Skye", "Initiator", "Australia", ["Regrowth", "Trailblazer", "Guiding Light", "Seekers"], "images/Skye.jpeg"),
    Agent("Yoru", "Duelist", "Japan", ["Fakeout", "Blindside", "Gatecrash", "Dimensional Drift"], "images/Yoru.jpeg"),
    Agent("Astra", "Controller", "Ghana" , ["Gravity Well" , "Nova Pulse" , "Nebula" , "Astral Form"] , "images/Astra.jpeg"),
    Agent("KAY/O" , "Initiator" , "Unknown (robot)" , ["FRAG/ment" ,"FLASH/drive" , "ZERO/point" , "NULL/cmd"] , "images/KAY:O.jpeg"),
    Agent("Chamber" , "Sentinel" , "France" , 	["Trademark" , 	"Headhunter" , 	["Rendezvous"] , ["Tour De Force"]], "images/Chamber.jpeg"),
    Agent("Neon", "Duelist", "Philippines", ["Fast Lane", "Relay Bolt", "High Gear", "Overdrive"], "images/Neon.jpeg"),
    Agent("Fade", "Initiator", "Turkey", ["Prowler", "Seize", "Haunt", "Nightfall"], "images/Fade.jpeg"),
    Agent("Harbor", "Controller", "India", ["Cove", "High Tide", "Cascade", "Reckoning"], "images/Harbor.jpeg"),
    Agent("Gekko", "Initiator", "USA", ["Dizzy", "Wingman", "Mosh Pit", "Thrash"], "images/Gekko.jpeg"),
    Agent("Deadlock", "Sentinel", "Norway", ["GravNet", "Sonic Sensor", "Barrier Mesh", "Annihilation"], "images/Deadlock.jpeg"),
    Agent("Iso", "Duelist", "China", ["Undercut", "Double Tap", "Kill Contract"], "images/Iso.jpeg"),
    Agent("Clove", "Controller", "Scotland", ["Pick-Me-Up", "Ruse", "Meddle" , 	"Not Dead Yet"] , 	"images/Clove.jpeg"),
]


# ===== RUN APP =====
if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(agents_data)
    app = QuizGUI(root, game)
    root.mainloop()
