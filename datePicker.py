from customtkinter import *
from tkcalendar import DateEntry
from tkinter import Tk, Label

def on_date_selected():
    selected_date = cal.get()
    selected_date_label.configure(text=f"Selected Date: {selected_date}")
    print(selected_date)

app = Tk()
app.geometry("400x300")
app.resizable(0, 0)

selected_date_label = CTkLabel(app, text="Selected Date: None")
selected_date_label.pack(pady=10)

cal = DateEntry(app, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.pack(pady=10)

select_date_button = CTkButton(app, text="Select Date", command=on_date_selected)
select_date_button.pack(pady=10)

app.mainloop()
