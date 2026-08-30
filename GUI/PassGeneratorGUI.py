import tkinter as tk
import random
import string

window = tk.Tk()
window.title("Password Generator")

varLetters = string.ascii_letters
varDigits = string.digits
varSpecialChars = string.punctuation

passWord = ""
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

def get_range():
    password_length = get_input_range.get()
    label_for_output.config(text="Your Password is...")
    output_label.config(text=password_length)
    get_input_range.delete(0, tk.END)

label = tk.Label(window, text="Enter Range Password")
label.pack(pady=10)

# Create an Entry widget for password input
get_input_range = tk.Entry(window)
get_input_range.pack()

# Button to trigger the function
submit_button = tk.Button(window, text="Done", command=get_range)
submit_button.pack(pady=10)

label_for_output = tk.Label(window, text="")
label_for_output.pack()
output_label = tk.Label(window, text="")
output_label.pack(pady=10)

window.mainloop()
