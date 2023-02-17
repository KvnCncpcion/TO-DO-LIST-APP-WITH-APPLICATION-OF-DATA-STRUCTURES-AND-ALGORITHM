print("********************PROGRAMMED BY*********************")
print("*************Kevin Joseph G. Concepcion***************")
print("**********************BSCOE 2-2***********************")

import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("595x667")
bg = PhotoImage(file = "background.png")
label = Label(root, image = bg)
label.place(x=-2,y=-2)
root.resizable(False,False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)

def clearallTask():
    global task_list
    listbox.delete(0,END)
    with open("tasklist.txt", 'w') as file:
        pass

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != "/n":
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file = open("tasklist.txt","w")
        file.close()


Image_icon = PhotoImage(file="images/task.png")
root.iconphoto(False,Image_icon)

TopImage = PhotoImage(file="images/topbar.png")
Label(root,image = TopImage, bg="#1A6457").pack()

dockImage = PhotoImage(file = "images/dock.png")
Label(root, image = dockImage, bg = "#1CB149").place(x = 75, y = 20)

noteImage = PhotoImage(file = "images/clipboard.png")
Label(root, image = noteImage, bg = "#8DC53C").place(x = 470, y = 20)

heading = Label(root, text = "ALL TASKS", font = "norwester 33",fg = "black",bg = "#64B44D")
heading.place(x = 190, y = 10)

frame = Frame(root,width=575,height=50,bg="#03093D")
frame.place(x=10,y=130)

task = StringVar()
task_entry = Entry(frame,width=50,font="norwester 23",bd=0,fg="black",bg="#64B44D")
task_entry.place(x=5,y=5.5)
task_entry.focus()

button = Button(frame,text="ADD",font="norwester 20",width=6,bg="#297061",fg="#fff",bd=0,command=addTask)
button.place(x=490,y=0)

frame1 = Frame(root,bd=3,width=850,height=280,bg="#03093D")
frame1.pack(pady=(120,0))

listbox = Listbox(frame1,font=("comic sans ms",11),width=40,height=16,bg="#64B44D",fg="black",cursor="hand2",selectbackground="#8EFF6D")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

Delete_icon = PhotoImage(file="images/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask,bg="#33A993").place(x=210,y=575)

clear_icon = PhotoImage(file="images/clear.png")
Button(root,image=clear_icon,bd=0,command=clearallTask,bg="#33A993").place(x=330,y=575)

root.mainloop()

#Reference Link: https://www.youtube.com/watch?v=T60cEaVYMJE