from  tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")

    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()

    elif text=="<--":
        scvalue.set(scvalue.get()[:-1])
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("644x900")
root.title("Calculator By Sharik")
root.wm_iconbitmap("2.ico")
root.configure(background="grey")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 30 bold")
screen.pack(fill=X, ipadx=8,padx=10,pady=10)

f = Frame(root, bg="black")

b = Button(f, text="9",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
# b.grid(row=1,column=0)
b.bind("<Button-1>",click)

b = Button(f, text="8",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="7",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root, bg="black")

b = Button(f, text="6",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="5",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="4",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)
f.pack()


f = Frame(root, bg="black")

b = Button(f, text="3",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="2",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="1",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="black")

b = Button(f, text="0",padx=30,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="-",padx=30,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="*",padx=30,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="black")

b = Button(f, text="/",padx=31,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="%",padx=26,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="=",padx=26,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="black")

b = Button(f, text="C",padx=26,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="+",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text="<--",padx=26,pady=16,font="lucida 25 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

b = Button(f, text=".",padx=28,pady=16,font="lucida 20 bold",activebackground="orange",activeforeground="white")
b.pack(side=LEFT,padx=18,pady=4)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()