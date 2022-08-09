import tkinter as tk
from tkinter import Label, PhotoImage,Text,Entry,Button
from os import listdir

window = tk.Tk()
window.geometry("500x500")
window.maxsize(width=500,height=500)
window.minsize(width=500,height=500)
window.title("Insta Code Generater")

def Generator():
    FileTitle = entry1.get()
    Video_Title = entry2.get()
    Iframe = entry3.get()
    output = txtarea.get("1.0","end-1c")
    
    print(output)


def text( text : str, posx : int, posy : int, win : tk = window ):
    Title : Label = Label(win,text=text)
    Title.pack(padx=posx,pady=posy)
file=listdir("./Pages")
text(f"Last generated file is : { file[-1] }",1,1)
text("Enter Title of the File : ",0,20)
entry1 = Entry(window,width=50)
entry1.pack()
text("Enter Title of the Video : ",20,20)
entry2 = Entry(window,width=50)
entry2.pack()
text("Enter The Iframe : ",20,20)
entry3 = Entry(window,width=50)
entry3.pack()
text("Output of the code",1,1)
txtarea = Text(window, height=10,width=50)
txtarea.pack()

btn1 = Button(window,text="Load",command=Generator)
btn1.pack()

tk.mainloop()
