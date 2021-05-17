from tkinter import *
import quiz_brain
THEME_COLOR = "#375362"




class QuizInterface:

    def __init__(self,quiz):

        self.window = Tk()
        self.window.title("qizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.minsize(300, 500)
        self.canvas = Canvas(height=250, width=300)
        self.quiz_data = quiz_brain.QuizBrain(quiz)



        self.question_text = self.canvas.create_text(125, 150, text="text", font=("ariel", 20, "bold"),
                                                     fill= THEME_COLOR)



        self.score_text = Label(text=f"score: {self.quiz_data.score} ", bg=THEME_COLOR, fg="white",
                                font=("ariel", 16, "bold"), padx=20, pady=20)
        self.score_text.grid(row=0, column=1)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_images = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_image)
        self.true_button.grid(row=2, column=0,pady=20,padx=20)

        self.false_button = Button(image=self.false_images)
        self.false_button.grid(row=2, column=1, pady=20, padx=20)

        self.canvas.grid(row=1, column=0, columnspan=2)

        self.window.mainloop()
