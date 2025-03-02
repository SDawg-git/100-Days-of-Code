from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image

picture_path = None
watermark_path = None

def select_picture():
    global picture_path
    picture_path = askopenfilename()

def select_watermark():
    global watermark_path
    watermark_path = askopenfilename()


def generate_picture():
    if picture_path is None:
        messagebox.showinfo(title="Select Picture", message="No Picture Selected!")
        return
    if watermark_path is None:
        messagebox.showinfo(title="Select Watermark", message="No Watermark Selected!")
        return

    photo = Image.open(picture_path)
    watermark = Image.open(watermark_path)

    width, height = photo.size
    resized_watermark = watermark.resize(size=(width, height))

    photo.paste(resized_watermark, (0,0), resized_watermark)
    photo.save("C:\\Users\\dzemo\\Desktop\\watermarked_photo.png")
    print("Photo Saved")


window = Tk()
window.minsize(width=200, height=100)
window.title("Watermark Applier")

frame = ttk.Frame(window, padding=10)
frame.grid()
ttk.Label(frame, text="Choose Photo to Watermark").grid(column=0, row=0)
ttk.Button(frame, text="Choose File", command=select_picture).grid(column=0, row=1)

ttk.Label(frame, text="Choose Watermark").grid(column=0, row=2)
ttk.Button(frame, text="Choose File", command=select_watermark).grid(column=0, row=3)

ttk.Label(frame, text="").grid(column=0, row=4)
ttk.Button(frame, text="Generate", command=generate_picture).grid(column=0, row=5)



window.mainloop()
