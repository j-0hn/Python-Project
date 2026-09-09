import tkinter as tk
from tkinter import messagebox
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

    found = False

    for translation_entry in translation:

        if translation_entry["english"].strip().lower() == english_text.strip().lower():

            translation_chinese = (
                translation_entry["chinese"] + " " +
                translation_entry["pinyin"]
            )

            output_text.delete("1.0", tk.END)
            output_text.insert("1.0", translation_chinese)

            found = True
            break

    if not found:
        messagebox.showwarning("Warning!", "No Translation yet!")
            
    

def clear_output():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

eng_frame = tk.Frame(root)
eng_frame.pack(pady=25)

label_english = tk.Label(eng_frame, text="English:")
label_english.pack(anchor="w")

# English Input field
input_text = tk.Text(eng_frame, height=5, width=40)
input_text.bind("<Return>", lambda event: translate_text(input_text.get("1.0", tk.END)))
input_text.pack(pady=10)

arrow = tk.Label(eng_frame, text="↓", font=("Arial", 25))
arrow.pack()

label_chinese = tk.Label(eng_frame, text="Chinese:")
label_chinese.pack(anchor="w")

# Chinese Output Text field
output_text = tk.Text(eng_frame, height=5, width=40)
output_text.pack(pady=10)

# Button Frame to make the button beside each other
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Translate Button
translate_button = tk.Button(button_frame, text="Translate", command=lambda: translate_text())
translate_button.pack(side="left", padx=5)

# Clear button
clear_btn = tk.Button(button_frame, text="Clear", command=clear_output)
clear_btn.pack(side="left", padx=5)

root.mainloop()