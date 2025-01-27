import tkinter as tk

# Resizable calculator window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.minsize(200, 300)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Result display
result = ""
entry_var = tk.StringVar()

# Result display layout
entry = tk.Entry(root, textvariable=entry_var, font="Arial 30", justify="right", bd=5)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Buttons
buttons = [('AC', 1, 0, 1), ('(', 1, 1, 1), (')', 1, 2, 1), ('/', 1, 3, 1),
           ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('*', 2, 3, 1),
           ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('-', 3, 3, 1),
           ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('+', 4, 3, 1),
           ('.', 5, 0, 1), ('0', 5, 1, 1), ('=', 5, 2, 2)]

# Buttons layout
for btn in buttons:
    text, row, column, columnspan = btn
    tk.Button(root, text=text, font="Arial 20", bd=2, command=lambda b=text: click(b)).grid(row=row, column=column, columnspan=columnspan, sticky="nsew", padx=2, pady=2)

# Button functionality
def click(char):
    global result
    if char == "=":
        try:
            result = str(eval(result))
        except:
            result = "Error"
    elif char == "AC":
        result = ""
    else:
        result += char
    entry_var.set(result)

root.mainloop()