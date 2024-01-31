from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
from Components.Dashboard_Frames.Dashboard_tab import tab_dashboard

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

CTkButton(master=sidebar_frame, text="tab1", fg_color="transparent", font=("Arial Bold", 14),
          hover_color="#207244", anchor="w",command = tab_dashboard(sidebar_frame)).pack(anchor="center", ipady=5, pady=(60, 0))

CTkButton(master=sidebar_frame, text="tab2", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55",
          hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

CTkButton(master=sidebar_frame, text="tab3", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55",
          hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(10, 0))

# Main view
main_view = CTkFrame(master=app, fg_color="#fff",
                     width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")




app.mainloop()
