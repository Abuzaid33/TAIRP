import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

class DocumentScannerApp:
    def __init__(self, master):
        self.master = master
        master.title("Document Scanner")

        self.label = tk.Label(master, text="Select an image file:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        image = cv2.imread(file_path)

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply Canny edge detection
        edged = cv2.Canny(blurred, 30, 150)

        # Find contours
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

        for contour in contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

        cv2.imwrite('scanned_document.jpg', image)  # Save the scanned document as an image

        cv2.imshow('Scanned Document', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentScannerApp(root)
    root.mainloop()
