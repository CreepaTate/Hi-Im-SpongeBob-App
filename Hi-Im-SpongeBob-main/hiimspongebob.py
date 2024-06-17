import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os
import threading
import ctypes

def force_exit():
    os._exit
    ctypes.windll.user32.MessageBoxW(0, "FATAL ERROR: ESCAPED ESCAPED ESCAPED", "Error", 1)



current_directory = os.getcwd()
# Initialize the pygame mixer
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load(os.path.join(current_directory, "hi-im-spongebob.mp3"))

# Play the MP3 file
pygame.mixer.music.play(-1)  # The -1 means to loop the song indefinitely

# Function to change the image and music
def selfaware():
    # Change the music
    pygame.mixer.music.load(os.path.join(current_directory, "1minutemark.mp3"))
    pygame.mixer.music.play(-1)
    
    # Change the image
    new_image = Image.open(os.path.join(current_directory, "uhoh.png"))
    new_photo = ImageTk.PhotoImage(new_image)
    label.config(image=new_photo)
    label.image = new_photo
    
def ending():
    # Change the music
    pygame.mixer.music.load(os.path.join(current_directory, "HI.mp3"))
    pygame.mixer.music.play(-1)
    
    # Change the image
    new_image = Image.open(os.path.join(current_directory, "endingscreen.png"))
    new_photo = ImageTk.PhotoImage(new_image)
    label.config(image=new_photo)
    label.image = new_photo
    label.configure(bg='#0078D7')

    # Make the window go into full screen mode
    root.attributes('-fullscreen', True)
    root.overrideredirect(True)
    
    # Call the force_exit function after 10 seconds
    threading.Timer(10, force_exit).start()


# Create the main window
root = tk.Tk()
root.title("spunchbop")

root.configure(bg='#0078D7')

# Load the icon
root.iconbitmap(os.path.join(current_directory, "spongebob.ico"))

# Load the SpongeBob image
spongebob_image = Image.open(os.path.join(current_directory, "spongebob.png"))
photo = ImageTk.PhotoImage(spongebob_image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.image = photo  # Keep a reference!
label.pack()

root.after(60000, selfaware)

root.after(120000, ending)

def close(event):
    root.destroy()

root.bind('<Escape>', close)

# Run the application
root.mainloop()
