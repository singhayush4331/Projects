import tkinter

window = tkinter.Tk()
window.title("Converter")
window.minsize(width=350, height=200)
window.config(padx=40, pady=40)


def button_clicked():
    miles = float(enter.get())
    km = str(miles * 1.6)
    my_label1.config(text=km)


# Label
my_label = tkinter.Label(text="is equal to", font=("Arial", 15,))
my_label.grid(column=0, row=1)

# Label1
my_label1 = tkinter.Label(text="0", font=("Arial", 15,))
my_label1.grid(column=1, row=1)

# Entry
enter = tkinter.Entry(width=15)
enter.grid(column=1, row=0)

# Label2
my_label2 = tkinter.Label(text="Miles", font=("Arial", 15,))
my_label2.grid(column=2, row=0)
my_label2.config(padx=5, pady=5)

# Label3
my_label3 = tkinter.Label(text="Km", font=("Arial", 15,))
my_label3.grid(column=2, row=1)
my_label3.config(padx=5, pady=5)

# Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
