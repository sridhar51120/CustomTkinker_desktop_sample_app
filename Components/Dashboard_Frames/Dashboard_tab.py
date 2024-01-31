from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
def tab_dashboard(app):
    print("Tab Dashboard")
    label_text = "Hello, CTkLabel!"
    label = CTkLabel(master=app, text=label_text, font=("Arial", 14))

    # Pack the label to display it in the window
    label.pack(pady=20)