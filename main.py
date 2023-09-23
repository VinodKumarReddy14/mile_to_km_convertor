import tkinter as t

window = t.Tk()
window.title(" Mile to Km Convertor ")
window.minsize(width=300, height=150)
window.config(padx=50, pady=30)


def calculate():
    miles = entry.get()
    km = round(float(miles)*1.609, 3)
    result_label.config(text=km)


entry = t.Entry()
entry.config(width=15)
entry.grid(column=1, row=0)

units_lab = t.Label(text="Miles")
units_lab.grid(column=2, row=0)
units_lab.config(padx=10)

label = t.Label(text="is equal to")
label.grid(column=0, row=1)
label.config(pady=10)

result_label = t.Label(text="0")
result_label.grid(column=1, row=1)
result_label.config(pady=10)

units_lab2 = t.Label(text="Km")
units_lab2.grid(column=2, row=1)
units_lab2.config(padx=10, pady=10)

button = t.Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()
