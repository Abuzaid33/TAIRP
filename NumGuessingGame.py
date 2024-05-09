import tkinter as tk
from tkinter import messagebox
import random

def check_number():
    user_guess = int(entry.get())
    if user_guess > computer_number:
        result_label.config(text="Guess is high")
    elif user_guess < computer_number:
        result_label.config(text="Guess is low")
    else:
        result_label.config(text="Congratulations! You guessed it right.")
        messagebox.showinfo("Congratulations", "You guessed the number correctly!")
        root.quit()

# Generate a random number between 1 and 100
computer_number = random.randint(1, 100)

# Create the Tkinter window
root = tk.Tk()
root.title("Number Guessing Game")

# Create GUI elements
label = tk.Label(root, text="Enter a number between 1 and 100:")
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=check_number)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
