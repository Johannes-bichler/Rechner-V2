from tkinter import *
import math
window=Tk()
VAR_OLD=""
OUTPUT_T=""
OUTPUT_R=""
list0 = ["+","-","*","/"]
list1 = ["=","^","sqrt","1/x","abs"]
output=Label(window, text=OUTPUT_T, borderwidth=2, relief="solid", height=3, width=45, anchor='w', padx=20, bg="white")
output.place(x=20, y=20)

def OUTPUT_CH():
    global VAR_OLD
    global OUTPUT_T
    output.config(text=OUTPUT_T)
def ONE(thr):
    global VAR_OLD
    global OUTPUT_T
    OUTPUT_T=str(OUTPUT_T)+str(1)
    output.config(text=OUTPUT_T)
    VAR_OLD=1
    OUTPUT_R=""
def TWO(thr):
    global VAR_OLD
    global OUTPUT_T
    OUTPUT_T=str(OUTPUT_T)+str(2)
    output.config(text=OUTPUT_T)
    VAR_OLD=2
    OUTPUT_R=""
def THREE(thr):
    global VAR_OLD
    global OUTPUT_T
    OUTPUT_T=str(OUTPUT_T)+str(3)
    output.config(text=OUTPUT_T)
    VAR_OLD=3
    OUTPUT_R=""
def FOUR(thr):
    global VAR_OLD
    global OUTPUT_T
    OUTPUT_T=str(OUTPUT_T)+str(4)
    output.config(text=OUTPUT_T)
    VAR_OLD=4
    OUTPUT_R=""
def FIVE(thr):
    global VAR_OLD
    global OUTPUT_T
    OUTPUT_T=str(OUTPUT_T)+str(5)
    output.config(text=OUTPUT_T)
    VAR_OLD=5
    OUTPUT_R=""
def SIX(thr):
    global VAR_OLD
    global OUTPUT_T
    OUTPUT_T=str(OUTPUT_T)+str(6)
    output.config(text=OUTPUT_T)
    VAR_OLD=6
    OUTPUT_R=""
def SEVEN(thr):
    global VAR_OLD
    global OUTPUT_T
    OUTPUT_T=str(OUTPUT_T)+str(7)
    output.config(text=OUTPUT_T)
    VAR_OLD=7
    OUTPUT_R=""
def EIGHT(thr):
    global VAR_OLD
    global OUTPUT_T
    OUTPUT_T=str(OUTPUT_T)+str(8)
    output.config(text=OUTPUT_T)
    VAR_OLD=8
    OUTPUT_R=""
def NINE(thr):
    global VAR_OLD
    global OUTPUT_T
    OUTPUT_T=str(OUTPUT_T)+str(9)
    output.config(text=OUTPUT_T)
    VAR_OLD=9
    OUTPUT_R=""
def NULL(thr):
    global VAR_OLD
    global OUTPUT_T
    if VAR_OLD=="/":
        output.config(text="Error: Division by 0.")
        output.after(1000, OUTPUT_CH)
    elif VAR_OLD=="":
        output.config(text="Error: Please do not start with 0.")
        output.after(1000, OUTPUT_CH)
    else:
        OUTPUT_T=str(OUTPUT_T)+str(0)
        output.config(text=OUTPUT_T)
        VAR_OLD=0
    OUTPUT_R=""
def PLUS(thr):
    global VAR_OLD
    global OUTPUT_T
    if VAR_OLD in list0:
        output.config(text="Error: repetitive modes")
        output.after(1000,OUTPUT_CH)
    elif VAR_OLD=="":
        output.config(text="Error: Cannot start with mode")
        output.after(1000,OUTPUT_CH)
    else:
        OUTPUT_T=str(OUTPUT_T)+str("+")
        output.config(text=OUTPUT_T)
        VAR_OLD="+"
    OUTPUT_R=""
def MINUS(thr):
    global VAR_OLD
    global OUTPUT_T
    if VAR_OLD in list0:
        output.config(text="Error: repetitive modes")
        output.after(1000,OUTPUT_CH)
    else:
        OUTPUT_T=str(OUTPUT_T)+str("-")
        output.config(text=OUTPUT_T)
        VAR_OLD="-"
    OUTPUT_R=""
def MULT(thr):
    global VAR_OLD
    global OUTPUT_T
    if VAR_OLD in list0:
        output.config(text="Error: repetitive modes")
        output.after(1000,OUTPUT_CH)
    elif VAR_OLD=="":
        output.config(text="Error: Cannot start with mode")
        output.after(1000,OUTPUT_CH)
    else:
        OUTPUT_T=str(OUTPUT_T)+str("*")
        output.config(text=OUTPUT_T)
        VAR_OLD="*"
    OUTPUT_R=""
def DIV(thr):
    global VAR_OLD
    global OUTPUT_T
    if VAR_OLD in list0:
        output.config(text="Error: repetitive modes")
        output.after(1000,OUTPUT_CH)
    elif VAR_OLD=="":
        output.config(text="Error: Cannot start with mode")
        output.after(1000,OUTPUT_CH)
    else:
        OUTPUT_T=str(OUTPUT_T)+str("/")
        output.config(text=OUTPUT_T)
        VAR_OLD="/"
    OUTPUT_R=""
def EQUALS(thr):
    global VAR_OLD
    global OUTPUT_T
    global OUTPUT_R
    OUTPUT_T=str(eval(OUTPUT_T))
    output.config(text=OUTPUT_T)
    OUTPUT_R=float(OUTPUT_T)
    VAR_OLD="="
def CLEAR(thr):
    global VAR_OLD
    global OUTPUT_T
    global OUTPUT_R
    output.config(text="Clear")
    OUTPUT_T=""
    OUTPUT_R=""
    VAR_OLD=""
    output.after(1000, OUTPUT_CH)
def SCI(thr):
    window.geometry("800x720+10+10")
def NORM(thr):
    window.geometry("400x720+10+10")
def QUAD(thr):
    global OUTPUT_T
    global OUTPUT_R
    global VAR_OLD
    global list1
    if VAR_OLD not in list1:
        output.config(text="Error: Unfinished Entry")
        output.after(1000, OUTPUT_CH)
    else:
        OUTPUT_T=str(OUTPUT_R*OUTPUT_R)
        output.config(text=OUTPUT_T)
        OUTPUT_R=float(OUTPUT_T)
        VAR_OLD="^"
def SQRT(thr):
    global OUTPUT_T
    global OUTPUT_R
    global VAR_OLD
    global list1
    if VAR_OLD not in list1:
        output.config(text="Error: Unfinished Entry")
        output.after(1000, OUTPUT_CH)
    else:
        OUTPUT_T=str(math.sqrt(OUTPUT_R))
        OUTPUT_R=float(OUTPUT_T)
        output.config(text=OUTPUT_T)
        VAR_OLD="sqrt"
def DEL(thr):
    global OUTPUT_T
    OUTPUT_T=OUTPUT_T[:-1]
    output.config(text=OUTPUT_T)
def FUNC(thr):
    global OUTPUT_T
    global OUTPUT_R
    global VAR_OLD
    global list1
    if VAR_OLD not in list1:
        output.config(text="Error: Unfinished Entry")
        output.after(1000, OUTPUT_CH)
    else:
        OUTPUT_T=str(1/OUTPUT_R)
        output.config(text=OUTPUT_T)
        OUTPUT_R=1/OUTPUT_R
        VAR_OLD="1/x"
def ABS(thr):
    global OUTPUT_T
    global OUTPUT_R
    global VAR_OLD
    global list1
    if VAR_OLD not in list1:
        output.config(text="Error: Unfinished Entry")
        output.after(1000, OUTPUT_CH)
    else:
        OUTPUT_T=str(abs(OUTPUT_R))
        OUTPUT_R=abs(OUTPUT_R)
        output.config(text=OUTPUT_T)
        VAR_OLD="abs"





        
window.bind("<Key-1>",ONE)
window.bind("<Key-2>",TWO)
window.bind("<Key-3>",THREE)
window.bind("<Key-4>",FOUR)
window.bind("<Key-5>",FIVE)
window.bind("<Key-6>",SIX)
window.bind("<Key-7>",SEVEN)
window.bind("<Key-8>",EIGHT)
window.bind("<Key-9>",NINE)
window.bind("<Key-0>",NULL)
window.bind("<plus>",PLUS)
window.bind("<minus>",MINUS)
window.bind("<Shift-*>",MULT)
window.bind("<Shift-/>",DIV)
window.bind("<Shift-=>",EQUALS)
window.bind("<Return>",EQUALS)
window.bind("<k>",SCI)
window.bind("<j>",NORM)



window.title('Rechner')
window.geometry("400x720+10+10")
window.resizable(width=False, height=False)


btn1=Button(window, text="1", fg='black', height=7, width=15, relief="solid", command=lambda: ONE(1))
btn1.place (x=20, y=80)

btn2=Button(window, text="2", fg='black', height=7, width=15, relief="solid", command=lambda: TWO(2))
btn2.place (x=140, y=80)

btn3=Button(window, text="3", fg='black', height=7, width=15, relief="solid", command=lambda: THREE(3))
btn3.place (x=260, y=80)

btn4=Button(window, text="4", fg='black', height=7, width=15, relief="solid", command=lambda: FOUR(4))
btn4.place (x=20, y=200)

btn5=Button(window, text="5", fg='black', height=7, width=15, relief="solid", command=lambda: FIVE(5))
btn5.place (x=140, y=200)

btn6=Button(window, text="6", fg='black', height=7, width=15, relief="solid", command=lambda: SIX(6))
btn6.place (x=260, y=200)

btn7=Button(window, text="7", fg='black', height=7, width=15, relief="solid", command=lambda: SEVEN(7))
btn7.place (x=20, y=320)

btn8=Button(window, text="8", fg='black', height=7, width=15, relief="solid", command=lambda: EIGHT(8))
btn8.place (x=140, y=320)

btn9=Button(window, text="9", fg='black', height=7, width=15, relief="solid", command=lambda: NINE(9))
btn9.place (x=260, y=320)

btn10=Button(window, text="+", fg='black', height=7, width=11, relief="solid", command=lambda: PLUS("+"))
btn10.place (x=20, y=560)

btn11=Button(window, text="-", fg='black', height=7, width=10, relief="solid", command=lambda: MINUS("-"))
btn11.place (x=110, y=560)

btn12=Button(window, text="*", fg='black', height=7, width=11, relief="solid", command=lambda: MULT("*"))
btn12.place (x=195, y=560)

btn13=Button(window, text="/", fg='black', height=7, width=11, relief="solid", command=lambda: DIV("/"))
btn13.place (x=287, y=560)

btn14=Button(window, text="0", fg='black', height=7, width=15, relief="solid", command=lambda: NULL(0))
btn14.place (x=20, y=440)

btn15=Button(window, text="=", fg='black', height=7, width=15, relief="solid", command=lambda: EQUALS("="))
btn15.place (x=140, y=440)

btn16=Button(window, text="C", fg='black', height=3, width=15, relief="solid", command=lambda: CLEAR("x"))
btn16.place (x=260, y=440)

btn17=Button(window, text="x^2",fg='black', height=7, width=15, relief="solid", command=lambda: QUAD("^2"))
btn17.place (x=420, y=80)

btn18=Button(window, text="K for Scientific View", fg='black', height=1, width=30, relief="solid", command=lambda: SCI("sci"))
btn18.place (x=20, y=680)

btn19=Button(window, text="J for normal View", fg='black', height=1, width=30, relief="solid", command=lambda:NORM("norm"))
btn19.place (x=420, y=680)

btn20=Button(window, text="DEL", fg='black', height=3, width=15, relief="solid", command=lambda:DEL("del"))
btn20.place (x=260, y=500)

btn21=Button(window, text="SQRT(x)", fg='black', height=7, width=15, relief="solid", command=lambda: SQRT("sqrt"))
btn21.place (x=540, y=80)

btn22=Button(window, text="1/x", fg='black', height=7, width=15, relief="solid", command=lambda: FUNC("1/x"))
btn22.place (x=660, y=80)

btn23=Button (window, text="|x|", fg="black", height=7, width=15, relief="solid", command=lambda: ABS("abs"))
btn23.place (x=420, y=200)

window.mainloop()


