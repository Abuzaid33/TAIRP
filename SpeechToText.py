import tkinter as tk
import speech_recognition as sr

class SpeechToTextApp:
    def __init__(self, master):
        self.master = master
        master.title("Speech to Text")

        self.label = tk.Label(master, text="Click 'Record' to start recording...")
        self.label.pack()

        self.record_button = tk.Button(master, text="Record", command=self.record)
        self.record_button.pack()

        self.text_output = tk.Text(master, height=10, width=50)
        self.text_output.pack()

    def record(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.label.config(text="Recording... Speak something...")
            audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data)
            self.text_output.delete(1.0, tk.END)  # Clear previous text
            self.text_output.insert(tk.END, text)
            self.label.config(text="Recording complete. Click 'Record' to record again.")
        except sr.UnknownValueError:
            self.label.config(text="Sorry, could not understand audio.")
        except sr.RequestError as e:
            self.label.config(text=f"Could not request results from Google Speech Recognition service; {e}")

def main():
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
