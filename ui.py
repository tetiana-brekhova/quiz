from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QUIZ")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quote_text = self.canvas.create_text(150, 125, text=f"some text", width=250, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.get_next_question()

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.push_true)
        self.true_button.grid(row=2, column=0)

        no_image = PhotoImage(file="images/false.png")
        self.no_button = Button(image=no_image, highlightthickness=0, bg=THEME_COLOR, command=self.push_false)
        self.no_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text, text=f"It's over!\nYour score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def push_true(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.get_feedback(is_right)

    def push_false(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score.config(text=f"score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

