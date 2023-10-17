import tkinter as tk

def miles_to_km():
    miles = float(miles_entry.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

window = tk.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_entry = tk.Entry(width=10)
miles_entry.grid(row=0, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_eq_label = tk.Label(text="is equal to")
is_eq_label.grid(row=1, column=0)

km_result_label = tk.Label(text="0")
km_result_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

conv_button = tk.Button(text="Convert", command=miles_to_km)
conv_button.grid(row=2, column=1)


window.mainloop()