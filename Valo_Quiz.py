import tkinter as tk
from tkinter import messagebox
import random

# ===== AGENT CLASS =====
class Agent:
    def __init__(self, name, role, origin, abilities):
        self.name = name
        self.role = role
        self.origin = origin
        self.abilities = abilities


# ===== QUIZ GAME CLASS =====
class QuizGame:
    def __init__(self, agents):
        self.agents = agents
        self.questions = []
        self.score = 0
        self.current_question = 0

    def generate_questions(self):
        questions = []

        for agent in self.agents:
            # Role question
            questions.append({
                "question": f"What is {agent.name}'s role?",
                "answer": agent.role
            })
            # Origin question
            questions.append({
                "question": f"Which country is {agent.name} from?",
                "answer": agent.origin
            })
            # Ability question
            ability = random.choice(agent.abilities)
            questions.append({
                "question": f"Which agent has the ability '{ability}'?",
                "answer": agent.name
            })

        random.shuffle(questions)
        self.questions = questions[:10]  # Only 10 questions

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


# ===== GUI =====
class QuizGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.player_name = ""

        self.root.title("Valorant Agent Quiz")
        self.root.geometry("600x400")

        # Welcome frame
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack(pady=50)

        tk.Label(self.welcome_frame, text="Enter your player name:", font=("Arial", 14)).pack(pady=10)
        self.name_entry = tk.Entry(self.welcome_frame, font=("Arial", 14))
        self.name_entry.pack(pady=10)
        tk.Button(self.welcome_frame, text="Start Quiz", font=("Arial", 14), command=self.start_quiz).pack(pady=10)

        # Quiz frame
        self.quiz_frame = tk.Frame(self.root)
        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 14), wraplength=500)
        self.question_label.pack(pady=20)
        self.answer_entry = tk.Entry(self.quiz_frame, font=("Arial", 14))
        self.answer_entry.pack(pady=10)
        self.submit_button = tk.Button(self.quiz_frame, text="Submit", font=("Arial", 14), command=self.submit_answer)
        self.submit_button.pack(pady=10)

    def start_quiz(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return

        self.player_name = name
        self.game.reset()

        self.welcome_frame.pack_forget()
        self.quiz_frame.pack(pady=50)

        self.show_question()

    def show_question(self):
        question = self.game.questions[self.game.current_question]['question']
        self.question_label.config(text=f"Q{self.game.current_question + 1}: {question}")
        self.answer_entry.delete(0, tk.END)

    def submit_answer(self):
        answer = self.answer_entry.get().strip()
        if answer.lower() in ("quit", "exit"):
            self.end_quiz()
            return

        correct = self.game.check_answer(answer)
        if correct:
            messagebox.showinfo("Result", "Correct!")
        else:
            correct_ans = self.game.questions[self.game.current_question]['answer']
            messagebox.showinfo("Result", f"Wrong! Correct answer: {correct_ans}")

        next_q = self.game.next_question()
        if next_q:
            self.show_question()
        else:
            self.end_quiz()

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


# ===== AGENTS DATA =====
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

# ===== RUN APP =====
if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(agents_data)
    app = QuizGUI(root, game)
    root.mainloop()
