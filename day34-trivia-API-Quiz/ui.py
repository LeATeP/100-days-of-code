from tkinter import *
from quiz_brain import QuizBrain
from threading import Timer

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain


        self.w = Tk()
        self.w.title("Quiz")
        self.w.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Hello",
                                                     font=("Ariel", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text=f"Score: {0}", fg="white", bg=THEME_COLOR, font=("Ariel", 15))
        self.score.grid(column=1, row=0)

        self.ok_image = PhotoImage(file="images/true.png")
        self.x_image = PhotoImage(file="images/false.png")

        self.ok_button = Button(image=self.ok_image, highlightthickness=0, command=self.true_answer)
        self.ok_button.grid(column=0, row=2)
        self.x_button = Button(image=self.x_image, highlightthickness=0, command=self.false_answer)
        self.x_button.grid(column=1, row=2)

        self.getting_question()

        self.w.mainloop()

    def true_answer(self):
        if self.quiz.still_has_questions():
            if self.quiz.check_answer("True"):
                self.highlight_answer(True)
            else:
                self.highlight_answer(False)

            self.score.config(text=f"Score: {self.quiz.score}")
            self.getting_question()
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of the quiz")

    def false_answer(self):
        if self.quiz.still_has_questions():
            if self.quiz.check_answer("False"):
                self.highlight_answer(True)
            else:
                self.highlight_answer(False)

            self.getting_question()
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of the quiz")

    def getting_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def turn_white(self):
        self.canvas.config(bg="white")
        
    def highlight_answer(self, answer: bool):
        t = Timer(0.15, self.turn_white)

        if answer:
            self.canvas.config(bg="green")
            t.start()
        else:
            self.canvas.config(bg="red")
            t.start()

