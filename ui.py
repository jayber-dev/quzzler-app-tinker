from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_ui = quiz_brain
        self.window = Tk()
        self.window.title("qizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.minsize(300, 600)
        self.canvas = Canvas(height=400, width=300)

        self.question_text = self.canvas.create_text(125, 200, text="",
                                                     font=("ariel", 20, "bold"),
                                                     fill=THEME_COLOR,
                                                     width="220"
                                                     )

        # self.score_text = Label(text=f"score: {self.quiz_ui.score} ", bg=THEME_COLOR, fg="white",
        #                         font=("ariel", 16, "bold"), padx=20, pady=20)
        # self.score_text.grid(row=0, column=1)
        self.true_image = PhotoImage(file="images/true.png")
        self.false_images = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_image, command=self.true_check)
        self.true_button.grid(row=2, column=0, pady=20, padx=20)

        self.false_button = Button(image=self.false_images, command=self.false_check)
        self.false_button.grid(row=2, column=1, pady=20, padx=20)

        self.canvas.grid(row=1, column=0, columnspan=2)
        self.get_question()

        if self.quiz_ui.still_has_questions():
            self.get_question()
        else:
            exit()
        self.window.mainloop()

    def get_question(self):
        q_text = self.quiz_ui.next_question()
        self.canvas.config(bg="white")
        # self.score_text.config(text=f"score: {self.quiz_ui.score} ")
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_check(self):
        score = self.quiz_ui.check_answer("true")
        self.give_feedback(score)
    def false_check(self):
        score = self.quiz_ui.check_answer("false")
        self.give_feedback(score)
    def give_feedback(self, score):
        if score:
            self.canvas.config(bg="green")
            self.window.after(300, self.more_questions)
        else:
            self.canvas.config(bg="red")
            self.window.after(300, self.more_questions)

    def more_questions(self):
        more_questions = self.quiz_ui.still_has_questions()
        if more_questions == False:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"great you finished your score is"
                                                            f" {self.quiz_ui.score} "
                                                            f"out of {self.quiz_ui.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.get_question()