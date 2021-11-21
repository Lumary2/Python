import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("Calculator")

calc_input=tk.Text(root, height=1, width=19, font=("Arial", 20))
calc_input.grid(columnspan=3)

result=""

def calc():
    result=eval(retrieve_input())#"1+2" -> 1+2
    calc_input.delete(1.0,"end")
    calc_input.insert(1.0,str(result))

def retrieve_input():
    input = calc_input.get("1.0",tk.END)
    return input

def input(number):
    calc_input.insert("end", str(number))

def clear():
    calc_input.delete(1.0,"end")


button_1=tk.Button(root,text="1",command=lambda:input(1),height=1,width=5,font=("Arial",18))
button_1.grid(row=1,column=0)
button_2=tk.Button(root,text="2",command=lambda:input(2),height=1,width=5,font=("Arial",18))
button_2.grid(row=1,column=1)
button_3=tk.Button(root,text="3",command=lambda:input(3),height=1,width=5,font=("Arial",18))
button_3.grid(row=1,column=2)
button_4=tk.Button(root,text="4",command=lambda:input(4),height=1,width=5,font=("Arial",18))
button_4.grid(row=2,column=0)
button_5=tk.Button(root,text="5",command=lambda:input(5),height=1,width=5,font=("Arial",18))
button_5.grid(row=2,column=1)
button_6=tk.Button(root,text="6",command=lambda:input(6),height=1,width=5,font=("Arial",18))
button_6.grid(row=2,column=2)
button_7=tk.Button(root,text="7",command=lambda:input(7),height=1,width=5,font=("Arial",18))
button_7.grid(row=3,column=0)
button_8=tk.Button(root,text="8",command=lambda:input(8),height=1,width=5,font=("Arial",18))
button_8.grid(row=3,column=1)
button_9=tk.Button(root,text="9",command=lambda:input(9),height=1,width=5,font=("Arial",18))
button_9.grid(row=3,column=2)
button_0=tk.Button(root,text="0",command=lambda:input(0),height=1,width=5,font=("Arial",18))
button_0.grid(row=4,column=0)

button_plus=tk.Button(root,text="+",command=lambda:input("+"),height=1,width=5,font=("Arial",18))
button_plus.grid(row=4,column=1)
button_minus=tk.Button(root,text="-",command=lambda:input("-"),height=1,width=5,font=("Arial",18))
button_minus.grid(row=4,column=2)
button_result=tk.Button(root,text="=",command=lambda:calc(),height=1,width=5,font=("Arial",18))
button_result.grid(row=5,column=0)

button_divide=tk.Button(root,text="/",command=lambda:input("/"),height=1,width=5,font=("Arial",18))
button_divide.grid(row=5,column=1)
button_multiply=tk.Button(root,text="*",command=lambda:input("*"),height=1,width=5,font=("Arial",18))
button_multiply.grid(row=5,column=2)
button_result=tk.Button(root,text="clear",command=lambda:clear(),height=1,width=5,font=("Arial",18),bg='#b42506',fg='white')
button_result.grid(row=6,column=1)

root.mainloop()

