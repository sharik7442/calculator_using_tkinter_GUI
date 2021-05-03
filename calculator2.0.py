from tkinter import *
from  tkinter.messagebox import *
# some useful variable
font=('verna',30,"bold")

# important function



def all_clear():
    textfield.delete(0,END)


def click_btn_function(event):
    global textfield
    print("btn clicked")
    b=event.widget
    text=b['text']

    if text=="x":
        textfield.insert(END,"*")
        return






    if text=="=":
        try:
           ex=textfield.get()
           anser=eval(ex)
           textfield.delete(0,END)
           textfield.insert(0,anser)
        except Exception as e:
            print("error...",e)
            showerror("Error",e)
        return
    textfield.insert(END, text)

# creating a window
window=Tk()
window.title("My Calculator")
window.geometry("584x650")
textfield=StringVar()
textfield.set("")
# picture label
window.wm_iconbitmap("1.ico")
pic=PhotoImage(file="image.png")
headingpic=Label(window,image=pic)
headingpic.pack(side=TOP)
# heading label
headinglabel=Label(window,text="My calculator",font=font,underline=0)
headinglabel.pack(side=TOP,pady=7)
# textfield
textfield=Entry(window,font=font,justify=CENTER)
textfield.pack(side=TOP,pady=8,fill=X,padx=8)

# button
buttonframe=Frame(window)
buttonframe.pack(side=TOP)

# adding button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonframe,text=str(temp),font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
        btn.grid(row=i,column=j,padx=3,pady=3)
        temp = temp + 1
        btn.bind('<Button-1>',click_btn_function)

zerobtn=Button(buttonframe,text="0",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
zerobtn.grid(row=3,column=0,padx=3,pady=3)

dotbtn=Button(buttonframe,text=".",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
dotbtn.grid(row=3,column=1,padx=3,pady=3)

equaltobtn=Button(buttonframe,text="=",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
equaltobtn.grid(row=3,column=2,padx=3,pady=3)

plusbtn=Button(buttonframe,text="+",font=font,width=5,relief=RIDGE)
plusbtn.grid(row=0,column=3,padx=3,pady=3)

minusbtn=Button(buttonframe,text="-",font=font,width=5,relief=RIDGE)
minusbtn.grid(row=1,column=3,padx=3,pady=3)

pbtn=Button(buttonframe,text="x",font=font,width=5,relief=RIDGE)
pbtn.grid(row=2,column=3,padx=3,pady=3)

dividebtn=Button(buttonframe,text="/",font=font,width=5,relief=RIDGE)
dividebtn.grid(row=3,column=3,padx=3,pady=3)

clearbtn=Button(buttonframe,text=".",font=font,width=10,relief=RIDGE,command=click_btn_function)
clearbtn.grid(row=4,column=0,padx=3,pady=3,columnspan=2)

plbtn=Button(buttonframe,text="AC",font=font,width=10,relief=RIDGE,command=all_clear)
plbtn.grid(row=4,column=2,padx=3,pady=3,columnspan=2)


# binding all button
plusbtn.bind('<Button-1>',click_btn_function)
minusbtn.bind('<Button-1>',click_btn_function)
zerobtn.bind('<Button-1>',click_btn_function)
equaltobtn.bind('<Button-1>',click_btn_function)
dotbtn.bind('<Button-1>',click_btn_function)
pbtn.bind('<Button-1>',click_btn_function)
clearbtn.bind('<Button-1>',click_btn_function)
dividebtn.bind('<Button-1>',click_btn_function)
plbtn.bind('<Button-1>',click_btn_function)



window.mainloop()