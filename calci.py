from tkinter import *
master = Tk()
master.title("Calculator")
master.geometry('440x550')
frame1 = Frame(master)
frame1.pack(fill=X)
frame2 = Frame(master)
frame2.pack(fill=X)
t = Canvas(frame1,height=100,width=450,bg = "Blue")
equation = []

def hos(flag,show):
    if flag=='H':
        #show.destroy()
        #show.grid_forget()
        show = Label(frame1,text="   \t\t\t\t\t",font=(30),bg="Blue")
        show.place(x=80,y=40)
    else:
        show.place(x=80,y=40)

def add(val):
    equation.append(val)
    #print(equation)
    txt = ""
    for i in equation:
        txt += i
    global show
    #print(txt)
    show = Label(frame1,text=txt,font=(20),bg="Blue")
    hos('S',show)
def clear():
    global equation
    equation=[]
    hos('H',show)
clr = Button(frame1,text="Clear",command=clear).place(x=10,y=40)
t.grid(row=0,column=0)

d9 =Button(frame2,text="9",width=8,height=5,font=(20),command=lambda: add('9'))
d8 =Button(frame2,text="8",width=8,height=5,font=(20),command=lambda: add('8'))
d7 =Button(frame2,text="7",width=8,height=5,font=(20),command=lambda: add('7'))
d6 =Button(frame2,text="6",width=8,height=5,font=(20),command=lambda: add('6'))
d5 =Button(frame2,text="5",width=8,height=5,font=(20),command=lambda: add('5'))
d4 =Button(frame2,text="4",width=8,height=5,font=(20),command=lambda: add('4'))
d3 =Button(frame2,text="3",width=8,height=5,font=(20),command=lambda: add('3'))
d2 =Button(frame2,text="2",width=8,height=5,font=(20),command=lambda: add('2'))
d1 =Button(frame2,text="1",width=8,height=5,font=(20),command=lambda: add('1'))
d0 =Button(frame2,text="0",width=8,height=5,font=(20),command=lambda: add('0'))
dp = Button(frame2,text="+",width=8,height=5,font=(20),command=lambda: add('+'))
dm = Button(frame2,text="-",width=8,height=5,font=(20),command=lambda: add('-'))
dmu = Button(frame2,text="*",width=8,height=5,font=(20),command=lambda: add('*'))
dd = Button(frame2,text="/",width=8,height=5,font=(20),command=lambda: add('/'))
#print(equation)
def evaluate(equation,show):
    solved = eval("".join(equation))
    #solved = calculation(equation)
    hos('H',show)
    showed = Label(frame1,text=solved,font=(20),bg="Blue")
    #print(solved)
    showed.place(x=80,y=40)
    #print(equation)
de = Button(frame2,text="=",width=8,height=5,font=(26),command = lambda: evaluate(equation,show))
d9.grid(row=1,column=0)
d8.grid(row=1,column=1)
d7.grid(row=1,column=2)
d6.grid(row=2,column=0)
d5.grid(row=2,column=1)
d4.grid(row=2,column=2)
d3.grid(row=3,column=0)
d2.grid(row=3,column=1)
d1.grid(row=3,column=2)
d0.grid(row=4,column=1)
de.grid(row=4,column=2)
dp.grid(row=1,column=3)
dm.grid(row=2,column=3)
dmu.grid(row=3,column=3)
dd.grid(row=4,column=3)
mainloop()
