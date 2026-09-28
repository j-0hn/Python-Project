import customtkinter as ctk
import random

ctk.set_appearance_mode("System")  # "Light", "Dark", or "System"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Match Game")

# This function will make the window center on the screen
def center_app(app, width, height):
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    app.geometry(f"{width}x{height}+{x}+{y}")
center_app(app, 300, 300)

theme_switch = ctk.CTkSwitch(
    app,
    text="",
    switch_width=30,
    switch_height=16,
    button_color="gray",
    button_hover_color="darkgray",
    command=lambda: ctk.set_appearance_mode(
        "Dark" if theme_switch.get() else "Light"
    ),
)
theme_switch.pack()

random_num1 = random.randint(1,10)
random_num2 = random.randint(1,10)

def answer_entry():
    get_answer = ctk.CTkEntry(app,
        placeholder_text="Answer here!"
    )
    get_answer.pack(pady=5)

def submit_button():
    submit_btn = ctk.CTkButton(app,
            text="Submit",
            command=submit_answer
    )
    submit_btn.pack()

def operator(operand):
   
    operand = operand_comboBox.get()
    if operand == "Addition":
        print("+")
        answer_entry()
        submit_button()
        
    elif operand == "Subtraction":
        print("-")
    elif operand == "Multiplication":
        print("*")
    else:
        print("/")
    
        
label = ctk.CTkLabel(app, text="Choose an Option")
label.pack()
option_operand = ["Addition", "Subtraction", "Multiplication", "Division"]
operand_comboBox = ctk.CTkComboBox(app, values=option_operand, command=operator)
operand_comboBox.pack()

def submit_answer():
    print("Hello!")



app.mainloop()