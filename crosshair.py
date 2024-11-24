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
    use_image_crosshair = os.path.exists("crosshair.png")

    print(r"""
 _______           _______ _________ _______  _______    _______  _______  _______  _______  _______           _______ _________ _______ 
(  ____ \|\     /|(  ____ \\__   __/(  ___  )(       )  (  ____ \(  ____ )(  ___  )(  ____ \(  ____ \|\     /|(  ___  )\__   __/(  ____ )
| (    \/| )   ( || (    \/   ) (   | (   ) || () () |  | (    \/| (    )|| (   ) || (    \/| (    \/| )   ( || (   ) |   ) (   | (    )|
| |      | |   | || (_____    | |   | |   | || || || |  | |      | (____)|| |   | || (_____ | (_____ | (___) || (___) |   | |   | (____)|
| |      | |   | |(_____  )   | |   | |   | || |(_)| |  | |      |     __)| |   | |(_____  )(_____  )|  ___  ||  ___  |   | |   |     __)
| |      | |   | |      ) |   | |   | |   | || |   | |  | |      | (\ (   | |   | |      ) |      ) || (   ) || (   ) |   | |   | (\ (   
| (____/\| (___) |/\____) |   | |   | (___) || )   ( |  | (____/\| ) \ \__| (___) |/\____) |/\____) || )   ( || )   ( |___) (___| ) \ \__
(_______/(_______)\_______)   )_(   (_______)|/     \|  (_______/|/   \__/(_______)\_______)\_______)|/     \||/     \|\_______/|/   \__/
                                                                                                                                         
 ______                       _        ______ _________          _                                                                       
(  ___ \ |\     /|  |\     /|| \    /\/ ___  \\__   __/|\     /|( (    /|                                                                
| (   ) )( \   / )  ( \   / )|  \  / /\/   \  \  ) (   | )   ( ||  \  ( |                                                                
| (__/ /  \ (_) /    \ (_) / |  (_/ /    ___) /  | |   | (___) ||   \ | |                                                                
|  __ (    \   /      \   /  |   _ (    (___ (   | |   |  ___  || (\ \) |                                                                
| (  \ \    ) (        ) (   |  ( \ \       ) \  | |   | (   ) || | \   |                                                                
| )___) )   | |        | |   |  /  \ \/\___/  /  | |   | )   ( || )  \  |                                                                
|/ \___/    \_/        \_/   |_/    \/\______/   )_(   |/     \||/    )_)                                                                
""")

    print(f"Crosshair Width: {size}")
    print(f"Using Image Crosshair: {use_image_crosshair}")

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

    if use_image_crosshair:
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
