import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 20,))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# New_Button
new_button = tkinter.Button(text="Click me", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry
enter = tkinter.Entry(width=10)
print(enter.get())
enter.grid(column=3, row=2)

window.mainloop()
