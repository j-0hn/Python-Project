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
center_window(root, 300, 200)

def calculate():
    try:
        weight = float(inputWeight.get())
        height = float(inputHeight.get()) / 100

        bmi = weight / (height * height)
        if bmi < 18.5:
            output_label.config(text=f"Your BMI is: {bmi: .1f} \nUnderweight")
            calc_button.config(text="Clear", command=clear_button)
            
        elif bmi >= 18.5 and bmi <= 24.9:
            output_label.config(text=f"Your BMI is: {bmi: .1f} \nNormal weight")
            calc_button.config(text="Clear", command=clear_button)
            
        elif bmi >= 25.0 and bmi <= 29.9:
            output_label.config(text=f"Your BMI is: {bmi: .1f} \nOverweight")
            calc_button.config(text="Clear", command=clear_button)
            
        else:
            output_label.config(text=f"Your BMI is: {bmi: .1f} \nObese")
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
    inputWeight.focus()

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

root.mainloop()