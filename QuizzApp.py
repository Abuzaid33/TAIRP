import tkinter as tk
from random import randint, choice

class MathsQuiz:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x500")
        self.master.title("Maths Quiz")

        self.question = tk.StringVar()
        self.answer = tk.StringVar()
        self.given_answer = tk.StringVar()
        self.score = tk.IntVar()
        self.question_number = tk.IntVar(value=0)

        self.create_widgets()
        self.generate_question()

    def create_widgets(self):
        self.heading_label = tk.Label(self.master, text="Maths Quiz", fg='blue', font=('arial', 25))
        self.heading_label.pack()

        self.question_label = tk.Label(self.master, textvariable=self.question, font=('arial', 20))
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.master, textvariable=self.given_answer, font=("arial", 20), width=25)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit", font=("arial", 15), command=self.check_answer)
        self.submit_button.pack()

        self.result_label = tk.Label(self.master, text='', font=('arial', 20))
        self.result_label.pack()

        self.score_label = tk.Label(self.master, text=f"Score: {self.score.get()}", font=('arial', 20), fg='blue')
        self.score_label.pack()

        self.restart_button = tk.Button(self.master, text="Restart", font=("arial", 15), command=self.restart, width=35)
        self.restart_button.pack()

    def generate_question(self):
        self.question_number.set(self.question_number.get() + 1)

        number1 = randint(1, 10)
        number2 = randint(1, 10)
        operator = choice(['+', '-', '*', '/'])

        self.question.set(f"{number1} {operator} {number2}")
        self.answer.set(eval(self.question.get()))

    def check_answer(self):
        if self.question_number.get() > 10:
            return

        if str(self.answer.get()) == self.given_answer.get():
            self.score.set(self.score.get() + 1)
            self.result_label.config(text='Correct', fg='green')
            self.score_label.config(text=f"Score: {self.score.get()}", fg='blue')
        else:
            self.result_label.config(text='Incorrect', fg='red')

        if self.question_number.get() == 10:
            self.result_label.config(text=f"Final Score: {self.score.get()}")
            self.submit_button.config(state='disabled')
        else:
            self.generate_question()

    def restart(self):
        self.score.set(0)
        self.question_number.set(0)
        self.score_label.config(text=f"Score: {self.score.get()}")
        self.submit_button.config(state='normal')
        self.result_label.config(text='')
        self.generate_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = MathsQuiz(root)
    root.mainloop()
