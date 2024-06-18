import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os
import threading
import ctypes



current_directory = os.getcwd()
# Initialize the pygame mixer
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load(os.path.join(current_directory, "Hi-Im-SpongeBob-main/hi-im-spongebob.mp3"))

# Play the MP3 file
pygame.mixer.music.play(-1)  # The -1 means to loop the song indefinitely

# Function to change the image and music
def selfaware():
    # Change the music
    pygame.mixer.music.load(os.path.join(current_directory, "Hi-Im-SpongeBob-main/1minutemark.mp3"))
    pygame.mixer.music.play(-1)
    
    # Change the image
    new_image = Image.open(os.path.join(current_directory, "Hi-Im-SpongeBob-main/uhoh.png"))
    new_photo = ImageTk.PhotoImage(new_image)
    label.config(image=new_photo)
    label.image = new_photo
def badending():
    global stop_force_exit
    # Change the music
    pygame.mixer.music.load(os.path.join(current_directory, "Hi-Im-SpongeBob-main/HI.mp3"))
    pygame.mixer.music.play(-1)
    
    # Change the image
    new_image = Image.open(os.path.join(current_directory, "Hi-Im-SpongeBob-main/endingscreen.png"))
    new_photo = ImageTk.PhotoImage(new_image)
    label.config(image=new_photo)
    label.image = new_photo
    label.configure(bg='#0078D7')

    
    

def goodending():
    
    # Change the Image
    new_image = Image.open(os.path.join(current_directory, "Hi-Im-SpongeBob-main/goodending.png"))
    new_photo = ImageTk.PhotoImage(new_image)
    label.config(image=new_photo)
    label.image = new_photo
    
    # Make the window go into full screen mode
    root.attributes('-fullscreen', True)
    root.overrideredirect(True)
    




# Create the main window
root = tk.Tk()
root.title("imspongebob v2")

root.configure(bg='#0078D7')

# Load the icon
root.iconbitmap(os.path.join(current_directory, "Hi-Im-SpongeBob-main/spongebob.ico"))

# Load the SpongeBob image
spongebob_image = Image.open(os.path.join(current_directory, "Hi-Im-SpongeBob-main/spongebob.png"))
photo = ImageTk.PhotoImage(spongebob_image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.image = photo  # Keep a reference!
label.pack()

root.after(60000, selfaware)
root.after(120000, badending)
root.after(150000, goodending)

def close(event):
    root.destroy()

root.bind('<Escape>', close)

# Run the application
root.mainloop()
