import tkinter as tk

# Functions
def press(num):
    expression.set(expression.get() + str(num))

def clear():
    expression.set("")

def backspace():
    expression.set(expression.get()[:-1])

def equal():
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("Error")

# Window Setup
root = tk.Tk()
root.title("Calculator")
root.geometry("330x470")
root.resizable(False, False)
root.config(bg="#2d2d2d")

expression = tk.StringVar()

# Entry Display
entry = tk.Entry(root, textvariable=expression, font=('Arial', 24), bg="#1e1e1e", fg="white", bd=0, justify="right")
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)

# Button Style
btn_config = {"font": ('Arial', 20), "bd": 0, "width": 4, "height": 1, "bg": "#3d3d3d", "fg": "white", "activebackground": "#555"}

# Buttons Grid
btns = [
    ('C', clear), ('⌫', backspace), ('%', lambda: press('%')), ('/', lambda: press('/')),
    ('7', lambda: press('7')), ('8', lambda: press('8')), ('9', lambda: press('9')), ('*', lambda: press('*')),
    ('4', lambda: press('4')), ('5', lambda: press('5')), ('6', lambda: press('6')), ('-', lambda: press('-')),
    ('1', lambda: press('1')), ('2', lambda: press('2')), ('3', lambda: press('3')), ('+', lambda: press('+')),
    ('0', lambda: press('0')), ('.', lambda: press('.')), ('=', equal)
]

# Render Buttons
frame = tk.Frame(root, bg="#2d2d2d")
frame.pack()
row, col = 0, 0
for (text, cmd) in btns:
    b = tk.Button(frame, text=text, command=cmd, **btn_config)
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        row += 1
        col = 0

root.mainloop()
