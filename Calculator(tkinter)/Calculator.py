from tkinter import*

expression=""

def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equal():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""

def clear():
    global expression
    expression=""
    equation.set(expression)

if __name__=="__main__":

    gui=Tk()
    gui.configure(background="pink")
    gui.title("calculator")
    gui.geometry("300x180")
    equation=StringVar()
    display=Entry(gui, textvariable=equation)
    display.grid(columnspan=5,ipadx=80,ipady=10)
    equation.set('Enter the numbers')


    button1 = Button(gui, text='1', fg='white', bg='purple', command=lambda : press(1), height=1, width=6)
    button1.grid(row=2,column=0)

    button2 = Button(gui, text='2', fg='white', bg='purple', command=lambda : press(2),height=1,width=6)
    button2.grid(row=2,column=1)

    button3 = Button(gui, text='3', fg='white', bg='purple', command=lambda : press(3),height=1,width=6)
    button3.grid(row=2,column=2)

    button4 = Button(gui, text='4', fg='black', bg='purple', command=lambda : press(4),height=1,width=6)
    button4.grid(row=3,column=0)

    button5 = Button(gui, text='5', fg='white', bg='purple', command=lambda : press(5),height=1,width=6)
    button5.grid(row=3,column=1)

    button6 = Button(gui, text='6', fg='white', bg='purple', command=lambda : press(6),height=1,width=6)
    button6.grid(row=3,column=2)

    button7 = Button(gui, text='7', fg='white', bg='purple', command=lambda : press(7),height=1,width=6)
    button7.grid(row=4,column=0)

    button8 = Button(gui, text='8', fg='white', bg='purple', command=lambda : press(8),height=1,width=6)
    button8.grid(row=4,column=1)

    button9 = Button(gui, text='9', fg='white', bg='purple', command=lambda : press(9),height=1,width=6)
    button9.grid(row=4,column=2)

    button0 = Button(gui, text='1', fg='white', bg='purple', command=lambda : press(0),height=1,width=6)
    button0.grid(row=5,column=1)

    button_plus = Button(gui, text='+', fg='white', bg='purple', command=lambda : press('+'),height=1,width=6)
    button_plus.grid(row=2,column=3)

    button_minus = Button(gui, text='-', fg='white', bg='purple', command=lambda : press('-'),height=1,width=6)
    button_minus.grid(row=3,column=3)

    button_multi = Button(gui, text='*', fg='white', bg='purple', command=lambda : press('*'),height=1,width=6)
    button_multi.grid(row=4,column=3)

    button_div = Button(gui, text='1', fg='white', bg='purple', command=lambda : press('/'),height=1,width=6)
    button_div.grid(row=5,column=3)

    button_dec = Button(gui, text='.', fg='white', bg='purple', command=lambda : press('.'),height=1,width=6)
    button_dec.grid(row=5,column=0)

    button_eq = Button(gui, text='=', fg='white', bg='purple', command=equal,height=1,width=6)
    button_eq.grid(row=5,column=2)

    button_clear = Button(gui, text='clear', fg='white', bg='purple', command=clear,height=1,width=6)
    button_clear.grid(row=6,columnspan=4,ipadx=37)

    button_op = Button(gui, text='(', fg='white', bg='purple', command=lambda: press('('), height=1, width=6)
    button_op.grid(row=6, column=0)

    button_cp = Button(gui, text=')', fg='white', bg='purple', command=lambda: press(')'), height=1, width=6)
    button_cp.grid(row=6, column=3)



gui.mainloop()