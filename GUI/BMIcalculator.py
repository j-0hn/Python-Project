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
center_window(root, 400, 400)




root.mainloop()