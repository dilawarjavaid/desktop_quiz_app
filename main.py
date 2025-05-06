import json
import tkinter as tk
import requests
from tkinter import messagebox

#Define the QuizApp Class and Initialize UI
class QuizApp:
    def __init__(self, root):
        # Fetch Quiz Data from a Remote URL
        def __init__(self, root):
            self.root = root
            self.root.title("Quiz Application")

            self.current_quiz = None
            self.current_question_index = 0
            self.score = 0

            self.title_label = tk.Label(root, text="Select a Quiz", font=('Helvetica', 18, 'bold'))
            self.title_label.pack(pady=20)

            self.quiz_buttons = []

            # Fetching quiz data from the provided URL
            url = "https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json"
            response = requests.get(url)
            if response.status_code == 200:
                quiz_data = response.json()
                for quiz in quiz_data['quizzes']:
                    btn = tk.Button(root, text=quiz['quizTitle'], font=('Helvetica', 14),
                                    command=lambda q=quiz: self.start_quiz(q))
                    btn.pack(pady=5)
                    self.quiz_buttons.append(btn)
            else:
                messagebox.showerror("Error", "Failed to fetch quiz data.")

            #Create question and option widgets
            self.question_label = tk.Label(root, text="", font=('Helvetica', 16), wraplength=400)
            self.question_label.pack(pady=20)

            self.choice_buttons = []
            for i in range(4):
                btn = tk.Button(root, text="", font=('Helvetica', 12), command=lambda c=i: self.check_answer(c))
                btn.pack(pady=5)
                self.choice_buttons.append(btn)

            self.reset_quiz()

    #Resets the quiz state.
    def reset_quiz(self):
        self.current_quiz = None
        self.current_question_index = 0
        self.score = 0
        self.title_label.config(text="Select a Quiz")
        for btn in self.quiz_buttons:
            btn.pack(pady=5)
        self.question_label.pack_forget()
        for btn in self.choice_buttons:
            btn.pack_forget()


    # Hides the quiz selection buttons.
    def start_quiz(self, quiz):
        self.current_quiz = quiz
        self.current_question_index = 0
        self.score = 0
        self.title_label.pack_forget()
        for btn in self.quiz_buttons:
            btn.pack_forget()
        self.question_label.pack(pady=20)
        for btn in self.choice_buttons:
            btn.pack(pady=5)
        self.show_question()


