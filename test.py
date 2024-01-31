# from lib.Databases.Database_connection import *
# from lib.Databases.DB import *
# from src import get_config

# # val = get_config("1")
# # print(val)

# try:
#     db_connection = Database_connection.get_connection()  
# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     if 'db_connection' in locals() and db_connection.is_connected():
#         db_connection.close()
#         print("Connection closed")

from customtkinter import *
from CTkTable import CTkTable
from PIL import Image

app = CTk()
app.geometry("856x645")
app.resizable(0, 0)

set_appearance_mode("light")

# Function to switch frames
def switch_frame(new_frame):
    global current_frame
    current_frame.pack_forget()
    new_frame.pack(expand=True, fill="both", padx=27, pady=21)
    current_frame = new_frame

# Sidebar
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

# ... (unchanged)

# Main view
main_view = CTkFrame(master=app, fg_color="#fff", width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

# Title frame
title_frame = CTkFrame(master=main_view, fg_color="transparent")
title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

# ... (unchanged)

# Metrics frame
metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
metrics_frame.pack(anchor="n", fill="x", padx=27, pady=(36, 0))

# ... (unchanged)

# Search container
search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
search_container.pack(fill="x", pady=(45, 0), padx=27)

# ... (unchanged)

# Initial table data
table_data = [
    ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
    ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed', '8'],
    ['6432', 'Laptop', 'Bob', '456 Elm St', 'Packing', '5'],
    # ... (more data)
]

# Initial table frame
table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
table_frame.pack(expand=True, fill="both", padx=27, pady=21)
table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
table.pack(expand=True)

# Set the initial frame
if 'current_frame' not in globals():
    current_frame = None
current_frame = table_frame

# Sidebar button functions
def show_dashboard():
    switch_frame(table_frame)

def show_orders():
    # Create a new frame for orders and switch to it
    orders_frame = CTkFrame(master=main_view, fg_color="transparent")
    orders_frame.pack(expand=True, fill="both", padx=27, pady=21)

    # Add widgets to the orders frame
    CTkLabel(master=orders_frame, text="Orders Page", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", side="left")

    # Switch to the new frame
    switch_frame(orders_frame)

# ... (add functions for other sidebar buttons)

# Dashboard button
CTkButton(master=sidebar_frame, image="analytics_img.png", text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=show_dashboard).pack(anchor="center", ipady=5, pady=(60, 0))

# Orders button
CTkButton(master=sidebar_frame, image="package_img.png", text="Orders", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55", hover_color="#eee", anchor="w", command=show_orders).pack(anchor="center", ipady=5, pady=(16, 0))

# ... (add buttons for other sections)

app.mainloop()
