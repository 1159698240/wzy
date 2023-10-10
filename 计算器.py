import tkinter as tk
root = tk.Tk()
root.geometry("295x280+150+150")
root.attributes("-alpha", 0.9)
root["background"] = "#ffffff"
result_num = tk.StringVar()
result_num.set(0)
lable1 = tk.Label(root,textvariable=result_num, width=20, height=2,font=('宋体', 20), justify=tk.LEFT,anchor=tk.SE)
lable1.grid(padx=4, pady=4, row=1, column=1, columnspan=4)
#第一行按钮
button_clear = tk.Button(root, text='C', width=5, font=('楷体', 16), relief=tk.FLAT, background='#C0C0C0')
button_back = tk.Button(root, text='←', width=5, font=('楷体', 16), relief=tk.FLAT, background='#C0C0C0')
button_division = tk.Button(root, text='/', width=5, font=('楷体', 16), relief=tk.FLAT, background='#C0C0C0')
button_multiplication = tk.Button(root, text='x', width=5, font=('楷体', 16), relief=tk.FLAT, background='#C0C0C0')
button_clear.grid(padx=4, pady=2, row=2, column=1)
button_back.grid(padx=4, pady=2, row=2, column=2)
button_division.grid(padx=4, pady=2, row=2, column=3)
button_multiplication.grid(padx=4, pady=2, row=2, column=4)
#第二行按钮
button_seven = tk.Button(root, text='7', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_eight = tk.Button(root, text='8', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_nine = tk.Button(root, text='9', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_subtraction = tk.Button(root, text='—', width=5, font=('楷体', 16), relief=tk.FLAT, background='#C0C0C0')
button_seven.grid(padx=4, pady=2, row=3, column=1)
button_eight.grid(padx=4, pady=2, row=3, column=2)
button_nine.grid(padx=4, pady=2, row=3, column=3)
button_subtraction.grid(padx=4, pady=2, row=3, column=4)
#第三行按钮
button_four = tk.Button(root, text='4', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_five = tk.Button(root, text='5', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_six = tk.Button(root, text='6', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_addition = tk.Button(root, text='+', width=5, font=('楷体', 16), relief=tk.FLAT, background='#C0C0C0')
button_four.grid(padx=4, pady=2, row=4, column=1)
button_five.grid(padx=4, pady=2, row=4, column=2)
button_six.grid(padx=4, pady=2, row=4, column=3)
button_addition.grid(padx=4, pady=2, row=4, column=4)
#第四行按钮
button_one = tk.Button(root, text='1', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_two = tk.Button(root, text='2', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_three = tk.Button(root, text='3', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_equal = tk.Button(root, text='=', width=5, height=3, font=('楷体', 16), relief=tk.FLAT, background='#C0C0C0')
button_one.grid(padx=4, pady=2, row=5, column=1)
button_two.grid(padx=4, pady=2, row=5, column=2)
button_three.grid(padx=4, pady=2, row=5, column=3)
button_equal.grid(padx=4, pady=2, row=5, rowspan=2, column=4)
#第五行按钮
button_zero = tk.Button(root, text='0', width=12, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_decimal = tk.Button(root, text='.', width=5, font=('楷体', 16), relief=tk.FLAT, background='#FFDEAD')
button_zero.grid(padx=4, pady=4, row=6, column=1, columnspan=2)
button_decimal.grid(padx=4, row=6, column=3)



lists = []
def append_num(i):
    lists.append(i)
    result_num.set(''.join(lists))

def operator(i):
    if len(lists) > 0:
        if lists[-1] in ['+', '-', '*', '/']:
            lists[-1] = i
        else:
            lists.append(i)
        result_num.set(''.join(lists))

def equal():
    a = ''.join(lists)
    end_num = eval(a)
    result_num.set(end_num)
    lists.clear()
    lists.append(str(end_num))

def clear():
    lists.clear()
    result_num.set(0)

def back():
    del lists[-1]
    result_num.set(lists)

button_clear.config(command=clear)
button_back.config(command=back)
button_division.config(command=lambda: operator('/'))
button_multiplication.config(command=lambda: operator('*'))
button_seven.config(command=lambda: append_num('7'))
button_eight.config(command=lambda: append_num('8'))
button_nine.config(command=lambda: append_num('9'))
button_subtraction.config(command=lambda: operator('-'))
button_four.config(command=lambda: append_num('4'))
button_five.config(command=lambda: append_num('5'))
button_six.config(command=lambda: append_num('6'))
button_addition.config(command=lambda: operator('+'))
button_one.config(command=lambda: append_num('1'))
button_two.config(command=lambda: append_num('2'))
button_three.config(command=lambda: append_num('3'))
button_equal.config(command=equal)
button_zero.config(command=lambda: append_num('0'))
button_decimal.config(command=lambda: append_num('.'))

root.mainloop()
