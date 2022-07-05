import os
from tkinter import *
import base64
from icon import img

root = Tk()
tmp = open("tmp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("tmp.ico")
os.remove("tmp.ico")

Label(root, text="hello world").pack()
root.mainloop()