from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title("image viewer")
root.geometry("800x800")
root.configure(background="black")

imagepath=""
def openimage():
    global imagepath
    imagepath=filedialog.askopenfilename(title="opentextfile",filetypes=[("Image Files","*.jpg *.gif *.png *.jpeg")])
    im=Image.open(imagepath)
    img=ImageTk.PhotoImage(im)
    label_image["image"]=img
    im.close()

def rotateimage():
    global imagepath
    im=Image.open(imagepath)
    img=ImageTk.PhotoImage(im.rotate(180))
    label_image["image"]=img
    im.close()
    

btn_open=Button(root,text="open image",command=openimage)
btn_open.place(relx=0.5,rely=0.25,anchor=CENTER)

label_image=Label(root)
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)

btn_rotate=Button(root,text="rote image",command=rotateimage)
btn_rotate.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()

