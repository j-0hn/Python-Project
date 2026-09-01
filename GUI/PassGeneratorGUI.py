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
#this function to run window in the center of screen
def center_window(window, width, height):
    #to get the actual pixels of my screen
    screen_width = window.winfo_screenwidth() 
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(window, 300, 300)

def generate_password(length):
    passWord = ""
    for i in range(int(length)):
        passWord += random.choice(varLetters + varDigits + varSpecialChars)
    return passWord

def get_range():
    passWord = ""
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
    
    passWord =generate_password(password_length)

    regenerate_password = password_length

    label_for_output.config(text="Your Password is...")
    output_label.config(text=passWord, font=("Arial", 20, "bold"))
    get_input_range.delete(0, tk.END)

    #regenerate = messagebox.askyesno("Generate Again?", "Do you want to generate another password?")
    #if regenerate:
     #   label_for_output.config(text="Password: ")
      #  output_label.config(text="passWord", font=("Arial", 12))

label = tk.Label(window, text="Enter Range Password")
label.pack(pady=10)

# Create an Entry widget for password input
get_input_range = tk.Entry(window, justify="center")
get_input_range.pack()

# Button to trigger the function
submit_button = tk.Button(window, text="Done", command=get_range)
submit_button.pack(pady=5, padx=20)

label_for_output = tk.Label(window, text="")
label_for_output.pack()
output_label = tk.Label(window, text="")
output_label.pack(pady=10)

window.mainloop()
