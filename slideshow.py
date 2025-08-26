from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import os
import time
import threading
import pygame

def create_slideshow(image_folder):
    image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith((".png", ".jpg", ".jpeg"))]
    current_image_index = 0

    def show_image(index):
        nonlocal current_image_index
        current_image_index = index % len(image_paths)
        img = Image.open(image_paths[current_image_index])
        img = img.resize((512, 512), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo

    def next_image():
        show_image(current_image_index + 1)

    def prev_image():
        show_image(current_image_index - 1)

    window = Tk()
    window.title("Image Slideshow")
    image_label = Label(window)
    image_label.pack()

    next_button = Button(window, text="Next", command=next_image)
    next_button.pack(side="right")

    prev_button = Button(window, text="Previous", command=prev_image)
    prev_button.pack(side="left")

    show_image(current_image_index)

    def play_audio():
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join("audio_output", "speech.mp3"))
        pygame.mixer.music.play()

    audio_thread = threading.Thread(target=play_audio, daemon=True)
    audio_thread.start()

    window.mainloop()

create_slideshow("generated")