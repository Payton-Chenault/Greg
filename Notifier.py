import customtkinter as ctk
import time

from PIL import Image
from customtkinter import CTkToplevel
from pygame import mixer

from RandomAsset import get_random_sound_path, get_random_picture_path

app = ctk.CTk()
app.withdraw()

mixer.init()

is_window_open = False

def close_warning(popup_window: CTkToplevel):
    global is_window_open
    popup_window.destroy()
    is_window_open = False
    app.quit()

def warn_user():
    global is_window_open

    if is_window_open:
        return
    is_window_open = True
    try:
        popup_sound = mixer.Sound(get_random_sound_path())
    except FileNotFoundError:
        print("Cant find sound")
        popup_sound = None
    popup = ctk.CTkToplevel(app)
    popup.title("TOO LOUD!")
    popup.geometry("400x400")
    popup.focus_force()
    popup.attributes("-topmost", True)
    popup.overrideredirect(True)
    if popup_sound:
        popup_sound.play()

    try:
        img_data = Image.open(get_random_picture_path())
        image = ctk.CTkImage(img_data, size=(400,400))
        image_label = ctk.CTkLabel(master=popup, image=image, text="")
        image_label.pack()
    except FileNotFoundError:
        error_lbl = ctk.CTkLabel(master=popup, text="YOU ARE TOO LOUD!", text_color="red", font=("Comic Sans", 24))
        error_lbl.pack(pady=150)

    popup.after(2000, lambda: close_warning(popup))

    app.mainloop()