#Shamini
#Task-2
#Calculator

import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = 0

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == 'x':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        
        result_var.set(str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title(" Shamini's Calculator")
root.geometry("300x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Calculator", font=("Arial", 16))
title_label.pack(pady=10)

tk.Label(root, text="Type Value 1:").pack()
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Type Value 2:").pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for symbol in ['+', '-', 'x', '/']:
    btn = tk.Button(button_frame, text=symbol, width=5, height=1, bg='green', fg='white',
                    font=("Arial", 12), command=lambda s=symbol: calculate(s))
    btn.pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Result:").pack(pady=5)
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, state="readonly")
result_entry.pack()

root.mainloop()
