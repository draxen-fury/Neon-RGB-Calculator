import tkinter as tk
import colorsys

# GUI Window Code
root = tk.Tk()
root.title('Neon RGB Calculator!')
root.geometry('400x650')
root.configure(bg='#121212')

# RGB Color Cycling
def rgb_cycle(widget):
    hue = 0
    def update_color():
        nonlocal hue
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)
        color = '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
        widget.config(fg=color)
        hue = (hue + 0.01) % 1
        root.after(50, update_color)
    update_color()

# Code to remove error message automatically
def dissapear_error():
    root.after(700, lambda: display.set(''))

# Code
def on_button_click(value):
    space = display.get()
    if value == 'AC':
        display.set('')
    elif value == '=':
        try:
            operation = space.replace("x", "*")
            result = eval(operation)
            display.set(result)
        except Exception as e:
            display.set("Error")
            dissapear_error()
    else:
        new_value = space + value
        display.set(new_value)


# Hover Effect
def on_hover(event):
    event.widget.config(bg='#00ffff', fg='black')

def on_leave(event):
    event.widget.config(bg='#1a1a1a', fg='#00ffff')

# Label
label = tk.Label(root, text='Neon RGB Calculator', font=('Arial', 24, 'bold'), bg='#121212', fg='white')
label.pack(pady=20)
rgb_cycle(label)

# Display Code
display = tk.StringVar()
display_area = tk.Label(root, font=('Arial', 36), textvariable=display, height=2, bg='#333333', fg='#00ffff')
display_area.pack(fill='both', padx=25, pady=20)

# Buttons Layout
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', 'AC', '=', '/'
]

# Buttons Frame
buttons_frame = tk.Frame(root, bg='#121212')
buttons_frame.pack(padx=20, pady=20)

# Buttons Logic
for z, button in enumerate(buttons):
    if button == 'AC':
        btn = tk.Button(buttons_frame, text=button, width=5, height=2, bg='#ff4d4d', fg='white', 
                        font=('Arial', 18, 'bold'), bd=0, activebackground='#ff4d4d', activeforeground='white')
    elif button == '=':
        btn = tk.Button(buttons_frame, text=button, width=5, height=2, bg='#4CAF50', fg='white', 
                        font=('Arial', 18, 'bold'), bd=0, activebackground='#4CAF50', activeforeground='white')
    else:
        btn = tk.Button(buttons_frame, text=button, width=5, height=2, bg='#1a1a1a', fg='#00ffff', 
                        font=('Arial', 18, 'bold'), bd=0, activebackground='#00ffff', activeforeground='black')
    
    row = z // 4
    column = z % 4
    btn.grid(row=row, column=column, padx=5, pady=5)
    btn.config(command=lambda x=button: on_button_click(x))
    
    if button not in ['AC', '=']:
        btn.bind("<Enter>", on_hover)
        btn.bind("<Leave>", on_leave)

# Application Start
root.mainloop()