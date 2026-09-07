import tkinter as tk
import json

root = tk.Tk()
root.title("English to Chinese Translator")

# This function will make the window center on the screen
def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
center_window(root, 400, 400)

def translate_text(english_text):
    with open("jsonFile/translation.json", "r") as file:
        translation = json.load(file)

    chinese_text = "haihai"
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", translation)

label = tk.Label(root, text="Enter English text to translate to Chinese:", font=("Arial", 12))
label.pack(pady=10)

# English Input field
input_text = tk.Text(root, height=8, width=40)
input_text.pack(pady=10)

translate_button = tk.Button(root, text="Translate", command=lambda: translate_text(input_text.get("1.0", tk.END)))
translate_button.pack(pady=10)

arrow = tk.Label(root, text="↓", font=("Arial", 25))
arrow.pack()

# Chinese Output Text field
output_text = tk.Text(root, height=8, width=40)
output_text.pack(pady=10)

root.mainloop()