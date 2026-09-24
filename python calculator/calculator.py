import tkinter as tk


# ==============================
# Create Main Window
# ==============================

window = tk.Tk()
window.title("Python Calculator")
window.geometry("400x550")
window.resizable(False, False)


# ==============================
# Display
# ==============================

display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bd=10,
    relief="ridge"
)

display.pack(
    fill="both",
    padx=15,
    pady=20,
    ipady=15
)


# ==============================
# Functions
# ==============================

# Add button value to display
def click_button(value):
    display.insert(tk.END, value)


# Clear everything
def clear_display():
    display.delete(0, tk.END)


# Delete one character
def delete_last():
    current = display.get()

    if current:
        display.delete(0, tk.END)
        display.insert(0, current[:-1])


# Calculate result
def calculate():
    try:
        expression = display.get()

        # Replace calculator symbols with Python operators
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by zero")

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# ==============================
# Button Frame
# ==============================

button_frame = tk.Frame(window)
button_frame.pack()


# ==============================
# Calculator Buttons
# ==============================

buttons = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("÷", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("×", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("−", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("%", 3, 2),
    ("+", 3, 3),
]


# ==============================
# Create Buttons
# ==============================

for text, row, column in buttons:

    if text == "−":
        command = lambda: click_button("-")

    elif text == "×":
        command = lambda: click_button("*")

    elif text == "÷":
        command = lambda: click_button("/")

    elif text == "%":
        command = lambda: click_button("/100")

    else:
        command = lambda value=text: click_button(value)

    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# ==============================
# Equal Button
# ==============================

equal_button = tk.Button(
    button_frame,
    text="=",
    font=("Arial", 18),
    width=5,
    height=2,
    command=calculate
)

equal_button.grid(
    row=4,
    column=0,
    columnspan=4,
    sticky="we",
    padx=5,
    pady=5
)


# ==============================
# Clear Button
# ==============================

clear_button = tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 16),
    width=15,
    height=2,
    command=clear_display
)

clear_button.pack(pady=10)


# ==============================
# Delete Button
# ==============================

delete_button = tk.Button(
    window,
    text="DELETE",
    font=("Arial", 16),
    width=15,
    height=2,
    command=delete_last
)

delete_button.pack()


# ==============================
# Keyboard Support
# ==============================

def keyboard_input(event):

    key = event.char

    # Numbers and operators
    if key in "0123456789.+-*/":
        click_button(key)

    # Enter key
    elif event.keysym == "Return":
        calculate()

    # Backspace key
    elif event.keysym == "BackSpace":
        delete_last()

    # Escape key
    elif event.keysym == "Escape":
        clear_display()


# Bind keyboard input
window.bind("<Key>", keyboard_input)


# ==============================
# Run Calculator
# ==============================

window.mainloop()