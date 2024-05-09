import tkinter as tk
from tkinter import messagebox

class PaymentApp:
    def __init__(self, master):
        self.master = master
        master.title("Payment Processor")

        self.label = tk.Label(master, text="Enter payment amount: $")
        self.label.pack()

        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()

        self.process_button = tk.Button(master, text="Process Payment", command=self.process_payment)
        self.process_button.pack()

    def process_payment(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Amount must be a positive number")
            
            # Simulate payment processing
            self.show_message("Payment Successful", f"Processing payment of ${amount}...\nPayment successful!")
        except ValueError as e:
            self.show_message("Payment Failed", f"Error: {e}\nPayment failed.")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()
