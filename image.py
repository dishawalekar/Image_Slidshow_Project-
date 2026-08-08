from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image Slideshow")

#list of image path
image_path=[
          r"C:\Users\Admin\Pictures\rhoit1.jpg",
          r"C:\Users\Admin\Pictures\rohit2.jfif",
          r"C:\Users\Admin\Pictures\rohit3.jfif",
          r"C:\Users\Admin\Pictures\rohit_saraf1.jpg",
          r"C:\Users\Admin\Pictures\rohit_saraf2.jfif",
          r"C:\Users\Admin\Pictures\rohit_saraf3.jpg"
]

#resize the image 1080x1080
image_size=(800,800)
images=[Image.open(path).resize(image_size) for path in image_path]
photo_images=[ImageTk.PhotoImage(image) for image in images]

# Create an iterator
label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image) 
        label.update()
        time.sleep(3) # Prevent garbage collection

slideshow=cycle(photo_images)

def start_slideshow():
    for _ in range (len(image_path)):
        update_image()

play_button=tk.Button(root,text="Play Slideshow",command=start_slideshow)
play_button.pack() 

root.mainloop()




