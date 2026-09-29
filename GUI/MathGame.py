import customtkinter as ctk
#from CTkMessagebox import CTkMessagebox
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

def random_numbers(operand):
    random_num1 = random.randint(1,10)
    random_num2 = random.randint(1,10)
    if operand == "Addition":
        question.configure(text=f"{random_num1} + {random_num2}")
    elif operand == "Subtraction":
        question.configure(text=f"{random_num1} - {random_num2}")


def operator(operand):
   
    operand = operand_comboBox.get()
    if operand == "Addition":
        print("+")
        random_numbers(operand)
        answer_entry()
        submit_button()
        
    elif operand == "Subtraction":
        random_numbers(operand)
        print("-")
    elif operand == "Multiplication":
        print("*")
    elif operand == "Division":
        print("/")
    else:
       question.configure(text="Please select an option!")
       app.after(3000, lambda: question.configure(text=""))
        
    
        
option_operand = ["Select an Option", "Addition", "Subtraction", "Multiplication", "Division"]
operand_comboBox = ctk.CTkComboBox(app, values=option_operand, command=operator)
operand_comboBox.pack()

question = ctk.CTkLabel(app, text="")
question.pack()




app.mainloop()