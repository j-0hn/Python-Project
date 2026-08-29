import tkinter as tk

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x400")

# Create an Entry widget for password input
get_input_range = tk.Entry(window)
get_input_range.pack(pady=5)

# Function to get the product value
def get_range():
    password_lenght = get_input_range.get()
    print("Product entered:", password_lenght)
    get_input_range.delete(0, tk.END)



# Button to trigger the function
submit_button = tk.Button(window, text="Done", command=get_range)
submit_button.pack(pady=10)

window.mainloop()
