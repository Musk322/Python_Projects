from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

#list of image path
image_paths = [
    r"C:\Users\muskan singh\OneDrive\Pictures\muskanclg.jpeg",
    r"C:\Users\muskan singh\OneDrive\Pictures\muskan12.jpg",
    r"C:\Users\muskan singh\OneDrive\Pictures\muskan 2.jpg",
    r"C:\Users\muskan singh\OneDrive\Pictures\muskan park.jpg",
    r"C:\Users\muskan singh\OneDrive\Pictures\muskan5.jpeg",
    r"C:\Users\muskan singh\OneDrive\Pictures\muskan7.jpeg",
] 

#Resize the images to 1080 * 1080
image_size = (1080,1080)
images = [Image.open(path). resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range (len(image_paths)):
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()