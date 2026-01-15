# import random
# import time

# class Agent:
#     def __init__(self, name, role, origin, abilities):
#         self.name = name
#         self.role = role
#         self.origin = origin
#         self.abilities = abilities


# class QuizGame:
#     def __init__(self, agents):
#         self.agents = agents
#         self.questions = []
#         self.score = 0
#         self.player_name = ""

#     def generate_questions(self):
#         questions = []

#         for agent in self.agents:
#             # Role question
#             questions.append({
#                 "question": f"What is {agent.name}'s role?",
#                 "answer": agent.role
#             })

#             # Origin question
#             questions.append({
#                 "question": f"Which country is {agent.name} from?",
#                 "answer": agent.origin
#             })

#             # Ability question
#             ability = random.choice(agent.abilities)
#             questions.append({
#                 "question": f"Which agent has the ability '{ability}'?",
#                 "answer": agent.name
#             })

#         random.shuffle(questions)
#         self.questions = questions

#     def play(self):
#         print("\n Welcome to the Valorant Agent Quiz! ")
#         print("---" * 30)
#         time.sleep(1)

#         self.player_name = input("Enter your player name: ").capitalize()
#         self.score = 0
#         self.generate_questions()

#         print("\n Type 'quit' anytime to exit the quiz.\n")

#         for i, q in enumerate(self.questions[:10], 1):
#             print(f"\nQ{i}. {q['question']}")
#             answer = input("Your answer: ").strip()

#             if answer.lower() in ("quit", "exit"):
#                 print("\n You exited the quiz early.")
#                 break

#             if answer.lower() == q["answer"].lower():
#                 print(" CORRECT!")
#                 self.score += 1
#             else:
#                 print(f" WRONG! Correct Answer: {q['answer']}")

#         print("---" * 20)
#         print(f" Quiz complete, {self.player_name}!")
#         print(f" Final Score: {self.score} / {i}")

#         if self.score >= 8:
#             print(" Rank: Valorant Pro")
#         elif self.score >= 5:
#             print(" Rank: Agent Trainee")
#         else:
#             print(" Rank: New Recruit")


# class Menu:
#     def __init__(self, game):
#         self.game = game

#     def show(self):
#         while True:
#             print("===" * 20)
#             print(" VALORANT AGENT QUIZ MENU ")
#             print("===" * 20)
#             print("1 Start Quiz")
#             print("2 Instructions")
#             print("3 Quit Game")
#             choice = input("\nEnter your choice (1/2/3): ").strip()

#             if choice == "1":
#                 self.game.play()
#             elif choice == "2":
#                 print("\n Instructions:")
#                 print("- You will be asked 10 random Valorant questions.")
#                 print("- Type your answer and press Enter.")
#                 print("- Type 'quit' anytime to exit the quiz.")
#             elif choice == "3":
#                 print("\n Thanks for playing! See you next time, Agent!")
#                 break
#             else:
#                 print(" Invalid choice, try again!")


# # ========= DATA SETUP =========
# agents_data = [
#     Agent("Jett", "Duelist", "South Korea", ["Cloudburst", "Updraft", "Tailwind", "Blade Storm"]),
#     Agent("Phoenix", "Duelist", "UK", ["Curveball", "Hot Hands", "Blaze", "Run It Back"]),
#     Agent("Reyna", "Duelist", "Mexico", ["Leer", "Devour", "Dismiss", "Empress"]),
#     Agent("Raze", "Duelist", "Brazil", ["Boom Bot", "Blast Pack", "Paint Shells", "Showstopper"]),
#     Agent("Yoru", "Duelist", "Japan", ["Fakeout", "Blindside", "Gatecrash", "Dimensional Drift"]),
#     Agent("Neon", "Duelist", "Philippines", ["Fast Lane", "Relay Bolt", "High Gear", "Overdrive"]),
#     Agent("Iso", "Duelist", "Unknown", ["Phase", "Pulse Grenade", "Flash Step", "Executioner"]),
#     Agent("Clove", "Duelist", "Unknown", ["Petal Trap", "Smokeblossom", "Vine Lash", "Blossom Barrage"]),
#     Agent("Waylay", "Duelist/Controller", "Unknown", ["Disruptor", "Smoke Charge", "Grapple", "Assault Protocol"]),
    
#     Agent("Sova", "Initiator", "Russia", ["Owl Drone", "Shock Bolt", "Recon Bolt", "Hunter's Fury"]),
#     Agent("Breach", "Initiator", "Sweden", ["Aftershock", "Flashpoint", "Fault Line", "Rolling Thunder"]),
#     Agent("Skye", "Initiator", "Australia", ["Regrowth", "Trailblazer", "Guiding Light", "Seekers"]),
#     Agent("KAY/O", "Initiator", "Unknown", ["FRAG/ment", "FLASH/drive", "ZERO/point", "NULL/cmd"]),
#     Agent("Fade", "Initiator", "Turkey", ["Prowler", "Seize", "Haunt", "Nightfall"]),
#     Agent("Gekko", "Initiator", "USA", ["Mosh Pit", "Dizzy", "Wingman", "Thrash"]),
#     Agent("Tejo", "Initiator", "Unknown", ["Flashbang", "Sensor Drone", "Magnet Mine", "Final Strike"]),
    
#     Agent("Brimstone", "Controller", "USA", ["Incendiary", "Stim Beacon", "Sky Smoke", "Orbital Strike"]),
#     Agent("Viper", "Controller", "USA", ["Snake Bite", "Poison Cloud", "Toxic Screen", "Viper's Pit"]),
#     Agent("Omen", "Controller", "Unknown", ["Shrouded Step", "Paranoia", "Dark Cover", "From the Shadows"]),
#     Agent("Astra", "Controller", "Ghana", ["Gravity Well", "Nova Pulse", "Nebula", "Astral Form"]),
#     Agent("Harbor", "Controller", "India", ["Cascade", "Cove", "High Tide", "Reckoning"]),
    
#     Agent("Sage", "Sentinel", "China", ["Barrier Orb", "Slow Orb", "Healing Orb", "Resurrection"]),
#     Agent("Cypher", "Sentinel", "Morocco", ["Trapwire", "Cyber Cage", "Spycam", "Neural Theft"]),
#     Agent("Killjoy", "Sentinel", "Germany", ["Nanoswarm", "Alarmbot", "Turret", "Lockdown"]),
#     Agent("Chamber", "Sentinel", "France", ["Trademark", "Headhunter", "Rendezvous", "Tour De Force"]),
#     Agent("Deadlock", "Sentinel", "Unknown", ["Sentry Mine", "Flux Trap", "Suppressor Field", "Containment"]),
#     Agent("Vyse", "Sentinel", "Unknown", ["Barrier Orb", "Tripwire", "Pulse Trap", "Reinforce"]),
#     Agent("Veto", "Sentinel", "Unknown", ["Minefield", "Signal Flare", "Control Grid", "Final Bastion"]),
# ]


# game = QuizGame(agents_data)
# menu = Menu(game)

# if __name__ == "__main__":
#     menu.show()
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
