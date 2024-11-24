import tkinter as tk
import pygetwindow as gw
from PIL import Image, ImageTk
import os

def get_circle_size():
    settings_file = "settings.txt"
    default_size = 3
    if os.path.exists(settings_file):
        try:
            with open(settings_file, "r") as file:
                size = int(file.readline().strip())
                return size
        except (ValueError, FileNotFoundError):
            pass
    return default_size

def create_overlay():
    size = get_circle_size()
    screen = gw.getWindowsWithTitle("Program Manager")[0]
    screen_width, screen_height = screen.width, screen.height

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.attributes("-transparentcolor", "black")
    root.config(bg="black")
    root.overrideredirect(True)

    center_x, center_y = screen_width // 2, screen_height // 2

    canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black", highlightthickness=0)

    if os.path.exists("crosshair.png"):
        try:
            image = Image.open("crosshair.png")
            image = image.resize((size, size), Image.Resampling.LANCZOS)
            crosshair_image = ImageTk.PhotoImage(image)
            canvas.create_image(center_x, center_y, image=crosshair_image)
        except Exception as e:
            print(f"Error loading crosshair.png: {e}")
    else:
        radius = size // 2
        canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="white", outline="white")

    canvas.pack()
    root.mainloop()

if __name__ == "__main__":
    create_overlay()
