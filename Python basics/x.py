import tkinter
import math

window = tkinter.Tk()
window.title("Converter")
window.minsize(width=350, height=200)
window.config(padx=40, pady=40)


def button_clicked():
    miles = float(enter.get()) #####
    km = str(math.floor(miles * 1.6)) ###################
    my_label.config(text=km)


# Label
my_label5 = tkinter.Label(text="is equal to", font=("Arial", 15,))
my_label5.grid(column=0, row=1)

# Label
my_label = tkinter.Label(text="0", font=("Arial", 15,))
# my_label = tkinter.Label(text=button_clicked(), font=("Arial", 15,))
my_label.grid(column=1, row=1)

# Entry
enter = tkinter.Entry(width=15)
# miles = enter.get()
enter.grid(column=1, row=0)

# Label
my_label1 = tkinter.Label(text="Miles", font=("Arial", 15,))
my_label1.grid(column=2, row=0)
my_label1.config(padx=5, pady=5)

# Label
my_label2 = tkinter.Label(text="Km", font=("Arial", 15,))
my_label2.grid(column=2, row=1)
my_label2.config(padx=5, pady=5)

# Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()