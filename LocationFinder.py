import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim

class LocationApp:
    def __init__(self, master):
        self.master = master
        master.title("Location App")

        self.label = tk.Label(master, text="Please enter your location (city, country, etc.):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Get Location", command=self.get_user_location)
        self.button.pack()

    def get_user_location(self):
        geolocator = Nominatim(user_agent="location_app")
        user_input = self.entry.get()

        try:
            user_location = geolocator.geocode(user_input)
            if user_location:
                messagebox.showinfo("Location Info", f"Latitude: {user_location.latitude}\nLongitude: {user_location.longitude}")
            else:
                messagebox.showerror("Error", "Location not found. Please try again.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LocationApp(root)
    root.mainloop()
