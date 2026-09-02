import tkinter as tk
from tkinter import messagebox
import random
import string

window = tk.Tk()
window.title("Password Generator")

varLetters = string.ascii_letters
varDigits = string.digits
varSpecialChars = string.punctuation

output_label = ""
label_for_output = ""
password_length = ""
reg_btn = None #this to access the regenerate button in other functions
copy_btn = None #need to declare as gobal to access the copy button in other functions
#this function to run window in the center of screen
def center_window(window, width, height):
    #to get the actual pixels of my screen
    screen_width = window.winfo_screenwidth() 
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(window, 300, 250)

def generate_password(length):
    passWord = ""
    for i in range(int(length)):
        passWord += random.choice(varLetters + varDigits + varSpecialChars)
    label_for_output.config(text="Your Password is...")
    output_label.config(text=passWord, font=("Arial", 20, "bold"))
    get_input_range.delete(0, tk.END)
   
def auto_generate_password(pword_length):
    passWord = generate_password(pword_length)  # Default length of 8 characters
    label_for_output.config(text="Your Password is...")
    output_label.config(text=passWord, font=("Arial", 20, "bold"))
    get_input_range.delete(0, tk.END)

def create_regenerate_btn(regenerate_password):
    global reg_btn
    reg_btn = tk.Button(window,
                        text="Regenerate Password",
                        command=lambda:
                        auto_generate_password(regenerate_password))
    reg_btn.pack(pady=5, padx=20)

def copy_password():
    password = output_label.cget("text")

    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        window.update()  # keeps clipboard after the app closes

def clear_output():
    output_label.config(text="")
    label_for_output.config(text="")
    get_input_range.delete(0, tk.END)
    get_input_range.config(state="normal")
    submit_button.config(text="Done", command=get_range)
    reg_btn.pack_forget()  # Hide the regenerate button when clearing output
    copy_btn.pack_forget()  # Hide the copy button when clearing output

def get_range():
    password_length = get_input_range.get()

    if not password_length.isdigit() or int(password_length) <= 0:
        messagebox.showwarning("Invalid Input",
                              "Please enter a valid positive integer for password length.")
        get_input_range.delete(0, tk.END)
        return #stops here if input is invalid
    
    elif int(password_length) < 4 or int(password_length) > 10:
        messagebox.showinfo("Invalid Input", "Password length must be between 4 and 10 characters.")
        get_input_range.delete(0, tk.END)
        return #stops here if input is invalid
    
    generate_password(password_length)
    create_regenerate_btn(password_length)
    submit_button.config(text="Clear Output", command=clear_output)
    get_input_range.config(state="disabled")

    global copy_btn
    copy_btn = tk.Button(
    window,
    text="Copy Password",
    command=copy_password)
    copy_btn.pack(pady=5)
    
label = tk.Label(window, text="Enter Range Password")
label.pack(pady=10)

# Create an Entry widget for password input
get_input_range = tk.Entry(window, justify="center")
get_input_range.pack()

# Button to trigger the function
submit_button = tk.Button(window, text="Done", command=get_range)
submit_button.pack(pady=5, padx=20)

# Label to display the generated password
label_for_output = tk.Label(window, text="")
label_for_output.pack()
output_label = tk.Label(window, text="")
output_label.pack(pady=10)

window.mainloop()
