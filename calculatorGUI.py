from tkinter import *


def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnClearDisp():
    global operator
    operator=""
    text_input.set("")
    
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
    
root=Tk()

root.title("Ubuntu Calculator")
operator=""
text_input=StringVar()

textDisplay=Entry(root,font=('arial',20,
                             'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="yellow",justify='right').grid(columnspan=4)
#==================================row1========================================================
btn7=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="yellow",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="yellow",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="yellow",command=lambda:btnClick(9)).grid(row=1,column=2)
btnplus=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="yellow",command=lambda:btnClick("+")).grid(row=1,column=3)
#=================================row2==========================================================
btn4=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="yellow",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="yellow",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="yellow",command=lambda:btnClick(6)).grid(row=2,column=2)
btnminus=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="yellow",command=lambda:btnClick("-")).grid(row=2,column=3)
#================================row3===========================================================
btn1=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="yellow",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="yellow",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="yellow",command=lambda:btnClick(3)).grid(row=3,column=2)
btnmultiply=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="yellow",command=lambda:btnClick("*")).grid(row=3,column=3)
#================================row4===========================================================
btn0=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="yellow",command=lambda:btnClick(0)).grid(row=4,column=0)
btnclear=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="yellow",command=lambda:btnClearDisp()).grid(row=4,column=1)
btnEquals=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="yellow",command=btnEqualsInput).grid(row=4,column=2)
btndivision=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="yellow",command=lambda:btnClick("/")).grid(row=4,column=3)
#================================completed design===============================================


root.mainloop()
