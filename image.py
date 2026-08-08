from itertools import cycle
from PIL import Image, ImageTk
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
image_cycle = cycle(photo_images)

label = tk.Label(root)
label.pack()

def update_image():
    photo = next(image_cycle)
    label.config(image=photo)
    label.image = photo  # Prevent garbage collection
    root.after(2000, update_image)  # Change image every 2 seconds

update_image()

root.mainloop()




