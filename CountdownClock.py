import tkinter as tk
import datetime

class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.end_time = None
        self.remaining_time = tk.StringVar()

        self.label = tk.Label(self.master, textvariable=self.remaining_time, font=('Arial', 18))
        self.label.pack()

        self.start_button = tk.Button(self.master, text="Start Countdown", command=self.start_countdown)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop Countdown", command=self.stop_countdown, state=tk.DISABLED)
        self.stop_button.pack()

        self.lap_button = tk.Button(self.master, text="Lap", command=self.record_lap, state=tk.DISABLED)
        self.lap_button.pack()

        self.update_clock()

    def start_countdown(self):
        self.end_time = datetime.datetime.now() + datetime.timedelta(minutes=5)  # Change 5 to your desired minutes
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.lap_button.config(state=tk.NORMAL)
        self.update_clock()  # Call update_clock to start the countdown immediately


    def stop_countdown(self):
        self.end_time = None
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.lap_button.config(state=tk.DISABLED)

    def record_lap(self):
        print("Lap recorded.")

    def calculate_remaining_time(self):
        if self.end_time is None:
            return datetime.timedelta(0)
        else:
            return self.end_time - datetime.datetime.now()

    def update_clock(self):
        remaining = self.calculate_remaining_time()
        if remaining.total_seconds() <= 0:
            self.remaining_time.set("00:00:00")
            self.stop_countdown()
            return
        else:
            hours, remainder = divmod(remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.remaining_time.set("{:02}:{:02}:{:02}".format(hours, minutes, seconds))
        self.master.after(1000, self.update_clock)



if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()
