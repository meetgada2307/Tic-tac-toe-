from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x400+0+0")
root.resizable(0,0)
root.title("TIC TAC TOE")

#################################################################

i=1

data = StringVar()
data.set("Player 1")

x=0

p1=0
p2=0
p3=0
p4=0
p5=0
p6=0
p7=0
p8=0
p9=0


#############################################################

def btn1clicked():
    global i
    global p1
    if (btn1 ["text"] == " ") and (i==1) :
        btn1["text"] = "X"
        i=2
        p1 = 1
        player()
        win()
        tie()
    else:
        if(btn1["text"]==" ")and(i==2):
            btn1["text"] = "O"
            i=1
            p1 = 2
            player()
            win2()
            tie()

def btn2clicked():
    global i
    global p2
    if (btn2 ["text"] == " ") and (i==1) :
        btn2["text"] = "X"
        i=2
        p2 = 1
        player()
        win()
        tie()
    else:
        if(btn2["text"]==" ")and(i==2):
            btn2["text"] = "O"
            i=1
            p2 = 2
            player()
            win2()
            tie()

def btn3clicked():
    global i
    global p3
    if (btn3 ["text"] == " ") and (i==1) :
        btn3["text"] = "X"
        i=2
        p3 = 1
        player()
        win()
        tie()
    else:
        if(btn3["text"]==" ")and(i==2):
            btn3["text"] = "O"
            i=1
            p3 = 2
            player()
            win2()
            tie()

def btn4clicked():
    global i
    global p4
    if (btn4 ["text"] == " ") and (i==1) :
        btn4["text"] = "X"
        i=2
        p4 = 1
        player()
        win()
        tie()
    else:
        if(btn4["text"]==" ")and(i==2):
            btn4["text"] = "O"
            i=1
            p4 = 2
            player()
            win2()
            tie()

def btn5clicked():
    global i
    global p5
    if (btn5 ["text"] == " ") and (i==1) :
        btn5["text"] = "X"
        i=2
        p5 = 1
        player()
        win()
        tie()
    else:
        if(btn5["text"]==" ")and(i==2):
            btn5["text"] = "O"
            i=1
            p5 = 2
            player()
            win2()
            tie()

def btn6clicked():
    global i
    global p6
    if (btn6 ["text"] == " ") and (i==1) :
        btn6["text"] = "X"
        i=2
        p6 = 1
        player()
        win()
        tie()
    else:
        if(btn6["text"]==" ")and(i==2):
            btn6["text"] = "O"
            i=1
            p6 = 2
            player()
            win2()
            tie()

def btn7clicked():
    global i
    global p7
    if (btn7 ["text"] == " ") and (i==1) :
        btn7["text"] = "X"
        i=2
        p7 = 1
        player()
        win()
        tie()
    else:
        if(btn7["text"]==" ")and(i==2):
            btn7["text"] = "O"
            i=1
            p7 = 2
            player()
            win2()
            tie()

def btn8clicked():
    global i
    global p8 
    if (btn8 ["text"] == " ") and (i==1) :
        btn8["text"] = "X"
        i=2
        p8 = 1 
        player()
        win()
        tie()
    else:
        if(btn8["text"]==" ")and(i==2):
            btn8["text"] = "O"
            i=1
            p8 = 2
            player()
            win2()

def btn9clicked():
    global i
    global p9
    if (btn9 ["text"] == " ") and (i==1) :
        btn9["text"] = "X"
        i=2
        p9 = 1
        player()
        win()
        tie()
    else:
        if(btn9["text"]==" ")and(i==2):
            btn9["text"] = "O"
            i=1
            p9 = 2
            player()
            win2()
            tie()

def player():
    global i
    global data
    global x
    if((i == 1)):
        data.set("Player 1")
        x=x+1
    else:
        if((i==2)and (x<8)):
            data.set("Player 2")
            x=x+1
        else:
            data.set(" ")
            
def tie():
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global i 
    if((p1!=0)and(p2!=0)and(p3!=0)and(p4!=0)and(p5!=0)and(p6!=0)and(p7!=0)and(p8!=0)and(p9!=0)):
        messagebox.showinfo("Tie","It's a tie")
        i=1
        player()
        reset()
        clear()


def win():
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global i
    if(((p1==1)and(p2==1)and(p3==1))or((p4==1)and(p5==1)and(p6==1))or((p7==1)and(p8==1)and(p9==1))or((p1==1)and(p4==1)and(p7==1))or((p2==1)and(p5==1)and(p8==1))or((p3==1)and(p6==1)and(p9==1))or((p1==1)and(p5==1)and(p9==1))or((p3==1)and(p5==1)and(p7==1))):
        #print("win 1")
        messagebox.showinfo("Win","Player 1 wins")
        clear()
        i=1
        player()
        reset()

def win2():
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global i
    if(((p1==2)and(p2==2)and(p3==2))or((p4==2)and(p5==2)and(p6==2))or((p7==2)and(p8==2)and(p9==2))or((p1==2)and(p4==2)and(p7==2))or((p2==2)and(p5==2)and(p8==2))or((p3==2)and(p6==2)and(p9==2))or((p1==2)and(p5==2)and(p9==2))or((p3==2)and(p5==2)and(p7==2))):
        messagebox.showinfo("Win","Player 2 wins")
        clear()
        i=2
        player()
        reset()
    
def clear():
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "

def reset():
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global x
    x=0
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    p6=0
    p7=0
    p8=0
    p9=0



#############################################################

btnrow1 = Frame(root)
btnrow1.pack(expand = TRUE, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = TRUE, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = TRUE, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = TRUE, fill = "both")


btn1 = Button(btnrow1, text=" ", font= ("Verdana",10),command=btn1clicked)
btn1.pack(side = LEFT,expand=TRUE,fill="both")

btn2 = Button(btnrow1, text=" ", font= ("Verdana",10),command=btn2clicked)
btn2.pack(side = LEFT,expand=TRUE,fill="both")

btn3 = Button(btnrow1, text=" ", font= ("Verdana",10),command=btn3clicked)
btn3.pack(side = LEFT,expand=TRUE,fill="both")


btn4 = Button(btnrow2, text=" ", font= ("Verdana",10),command=btn4clicked)
btn4.pack(side = LEFT,expand=TRUE,fill="both")

btn5 = Button(btnrow2, text=" ", font= ("Verdana",10),command=btn5clicked)
btn5.pack(side = LEFT,expand=TRUE,fill="both")

btn6 = Button(btnrow2, text=" ", font= ("Verdana",10),command=btn6clicked)
btn6.pack(side = LEFT,expand=TRUE,fill="both")


btn7 = Button(btnrow3, text=" ", font= ("Verdana",10),command=btn7clicked)
btn7.pack(side = LEFT,expand=TRUE,fill="both")

btn8 = Button(btnrow3, text=" ", font= ("Verdana",10),command=btn8clicked)
btn8.pack(side = LEFT,expand=TRUE,fill="both")

btn9 = Button(btnrow3, text=" ", font= ("Verdana",10),command=btn9clicked)
btn9.pack(side = LEFT,expand=TRUE,fill="both")

lbl = Label(btnrow4, text = "Label", anchor=N, font = ("Verdana",18,"bold"),textvariable = data)
lbl.pack(expand=TRUE , fill="both")




root.mainloop()