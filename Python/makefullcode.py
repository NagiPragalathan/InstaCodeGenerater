import io
from random import choice
from justtry import Simple,hard, ORD_Type,others
from tools import HTML_Aliner,colors
from assats import assgin
# import pyperclip as pc

counts = {"1":15,"2":4,"3":5,"4":2}
type_=[]
stepc = {}

input_str = """She Tells Him Ooh love ❤️
no one's ever gonna hurt❤‍🩹 you love 
i am gonna give you all my love💝
nobody matters like you🙂
┻┳|―-∩
┳┻|        ヽ
┻┳|    ●    |
┳┻|▼) _ノ
┻┳|￣    )
┳ﾐ(￣ ／
┻┳T￣|""".split("\n")


def MakeCode(String):
    choose = ""
    steps:str=""
    code:str=""
    for i in String:
        type = choice(range(1,len(counts)+1))
        if(type == 1):
            opt = choice(range(1,counts.get("1")+1))
            choose= Simple(i,opt)
            code = code +choose + "\n"
        elif(type == 2):
            opt = choice(range(2,counts.get("2")+1))
            choose= hard(i,opt)
            code = code + hard(i,opt) + "\n"
        elif(type == 3):
            opt = choice(range(1,counts.get("3")+1))
            choose= ORD_Type(i,opt)
            code = code + ORD_Type(i,opt) + "\n"
        elif(type == 4):
            opt = choice(range(1,counts.get("4")+1))
            choose= others(i,opt)
            code = code + others(i,opt) + "\n"
        steps=steps+choose+"\n"
        stepc[i]=choose
    return steps



# print(colors(HTML_Aliner(store)))
def Steps():
    StepHTML=""
    for i,x in enumerate(input_str):
        StepHTML = StepHTML+f"""<div class="con">
                                <div class="num">
                                    <h1>{i+1}</h1>
                                </div>
                                <div class="conta">
                                    <div class="divh1">
                                        <h2>{x}</h2>
                                    </div>
                                    <div class="control">
                                        <p>{colors(HTML_Aliner(stepc.get(x)))}</p>
                                    </div>
                                </div>
                            </div>\n"""

    return StepHTML
            


a="Day6"

def Maker(Output,FullCode,Step,store,title,videoTitle,iframe):
    index = assgin(title,videoTitle,iframe)

    code = index[0] + ( Output ) + index[1] + ( FullCode ) + index[2] + ( Step ) + index[3] + ( store )+ index[4]
    
    
    # pc.copy(code)

    with io.open(f"./Pages/{title}.html","w",encoding='utf8') as f:
        for i in code:
            f.write(i)
    f.close()
    with io.open("./Python/test.py","w",encoding='utf8') as d:
        print(store)
        for j in store:
            d.write(j)
    d.close()
    
    
store = MakeCode(input_str)
Output = "</br>".join(input_str)
FullCode = colors(HTML_Aliner(store))
Step = Steps()
Maker(Output,FullCode,Step,store,"Day4","She Tells Him Ooh love song coding version","Iframe")
print(store)
    
# #GUI  Window


# import tkinter as tk
# from tkinter import Label, PhotoImage,Text,Entry,Button
# from os import listdir

# window = tk.Tk()
# window.geometry("500x500")
# window.maxsize(width=500,height=500)
# window.minsize(width=500,height=500)
# window.title("Insta Code Generater")

# def Generator():
    
#     #Output Source
#     Output = "</br>".join(input_str)
#     FullCode = colors(HTML_Aliner(store))
#     Step = Steps()
    
#     FileTitle = entry1.get()
#     Video_Title = entry2.get()
#     Iframe = entry3.get()
#     output = txtarea.get("1.0","end-1c")
#     Maker(Output,FullCode,Step,store,FileTitle,Video_Title,Iframe)
    


# def text( text : str, posx : int, posy : int, win : tk = window ):
#     Title : Label = Label(win,text=text)
#     Title.pack(padx=posx,pady=posy)
# file=listdir("./Pages")
# try:
#     text(f"Last generated file is : { file[-1] }",1,1)
# except:
#     pass
# text("Enter Title of the File : ",0,20)
# entry1 = Entry(window,width=50)
# entry1.pack()
# text("Enter Title of the Video : ",20,20)
# entry2 = Entry(window,width=50)
# entry2.pack()
# text("Enter The Iframe : ",20,20)
# entry3 = Entry(window,width=50)
# entry3.pack()
# text("Output of the code",1,1)
# txtarea = Text(window, height=10,width=50)
# txtarea.pack()

# btn1 = Button(window,text="Load",command=Generator)
# btn1.pack()

# tk.mainloop()
