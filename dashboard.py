from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
from Components.Dashboard_Frames.Dashboard import tab_dashboard
from Components.Dashboard_Frames.Products import tab_products

app = CTk()
app.geometry("856x645")
app.resizable(0, 0)
set_appearance_mode("light")


def switch_frame(new_frame):
    global current_frame
    current_frame.pack_forget()
    new_frame.pack(expand=True, fill="both", padx=27, pady=21)
    current_frame = new_frame


# Sidebar
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55",
                         width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")


# Main view
main_view = CTkFrame(master=app, fg_color="#fff",
                     width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")


CTkButton(master=sidebar_frame, text="Dashboard", fg_color="#fff", font=("Arial Bold", 14),
          hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))
# ,command = tab_dashboard(main_view)

CTkButton(master=sidebar_frame, text="Products", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55",
          hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(40, 0))
# ,command = tab_products(main_view)
CTkButton(master=sidebar_frame, text="Billing", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55",
          hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(40, 0))

CTkButton(master=sidebar_frame, text="Selling", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55",
          hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(40, 0))

CTkButton(master=sidebar_frame, text="Profile", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55",
          hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(40, 0))






app.mainloop()