import tkinter as tk
import re

class CreditCardValidatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Credit Card Validator")

        self.label = tk.Label(master, text="Enter your credit card number:")
        self.label.pack()

        self.card_number_entry = tk.Entry(master)
        self.card_number_entry.pack()

        self.validate_button = tk.Button(master, text="Validate", command=self.validate_credit_card)
        self.validate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def validate_credit_card(self):
        card_number = self.card_number_entry.get()

        # Remove non-numeric characters from the input
        card_number = re.sub(r'\D', '', card_number)

        # Check if the card number is 16 digits long and contains only digits
        if len(card_number) != 16 or not card_number.isdigit():
            self.result_label.config(text="Invalid credit card number.")
            return

        # Apply the Luhn algorithm to validate the card
        total = 0
        for i, digit in enumerate(card_number[::-1]):
            num = int(digit)
            total += num if i % 2 == 0 else num * 2 - 9 if num * 2 > 9 else num * 2

        if total % 10 == 0:
            self.result_label.config(text="Valid credit card number!")
        else:
            self.result_label.config(text="Invalid credit card number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CreditCardValidatorApp(root)
    root.mainloop()
