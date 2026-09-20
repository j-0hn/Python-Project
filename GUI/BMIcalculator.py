import tkinter as tk

root = tk.Tk()
root.title("BMI Calculator")

# This function will make the window center on the screen
def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
center_window(root, 300, 300)

def calculate():
    try:
        weight = float(inputWeight.get())
        height = float(inputHeight.get()) / 100

        bmi = weight / (height * height)
        output_label.config(text=f"Your BMI is: {bmi: .1f}")

        calc_button.config(text="Clear", command=clear_button)

        root.focus()
    except ValueError:
        output_label.config(text="Please enter numbers only!")
        inputWeight.delete(0, tk.END)
        inputHeight.delete(0, tk.END)
        inputWeight.focus()
        root.after(3000, lambda: output_label.config(text="")) # to disappear automatically
    
def go_to_height():
    inputHeight.focus()

def clear_button():
    inputWeight.delete(0, tk.END)
    inputHeight.delete(0, tk.END)
    output_label.config(text="")
    calc_button.config(text="Calculate", command=calculate)

label_weight = tk.Label(root, text="Weight in (kg)")
label_weight.pack()

inputWeight = tk.Entry(root)
inputWeight.bind("<Return>", lambda event: go_to_height())
inputWeight.pack()

label_height = tk.Label(root, text="Height in (cm)")
label_height.pack()

inputHeight = tk.Entry(root)
inputHeight.bind("<Return>", lambda event: calculate())
inputHeight.pack()

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack()

output_label = tk.Label(root, text="")
output_label.pack(padx=5, pady=5)

# table showing info of BMI
table = tk.Frame(root)
table.pack(padx=10, pady=10)

label1 = tk.Label(table, text="BMI")
label1.grid(row=0, column=0)

label2 = tk.Label(table, text="Category")
label2.grid(row=0, column=1)

label3 = tk.Label(table, text="< 18.5")
label3.grid(row=1, column=0)

label4 = tk.Label(table, text="Underweight")
label4.grid(row=1, column=1)

label5 = tk.Label(table, text="18.5–24.9")
label5.grid(row=2, column=0)

label6 = tk.Label(table, text="Normal weight")
label6.grid(row=2, column=1)

label7 = tk.Label(table, text="25.0–29.9")
label7.grid(row=3, column=0)

label8 = tk.Label(table, text="Overweight")
label8.grid(row=3, column=1)

label9 = tk.Label(table, text="≥ 30")
label9.grid(row=4, column=0)

label10 = tk.Label(table, text="Obese")
label10.grid(row=4, column=1)

root.mainloop()