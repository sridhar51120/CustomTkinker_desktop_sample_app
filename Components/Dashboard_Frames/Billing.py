import tkinter as tk
from tkinter import ttk
from customtkinter import *

def add_data(tree):
    entry_order_id = input("Enter S.NO: ")
    entry_item_name = input("Enter Item Name: ")
    entry_quantity = input("Quantity: ")
    entry_count = input("Enter Count: ")
    entry_price = input("Enter Price: ")
    tree.insert("", "end", values=(entry_order_id, entry_item_name, entry_quantity, entry_count, entry_price))
    print("Row Completed")

def tab_billing(main_view):
    columns = ["S.No", "Item Name","Quantity", "Count", "Price"]
    tree = ttk.Treeview(main_view, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col, anchor=tk.CENTER)
        tree.column(col, width=150, anchor=tk.CENTER)
    
    heading = ttk.Style()
    heading.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#FFFFFF", foreground="#000000", anchor="center")
    
    tree_style = ttk.Style()
    tree_style.configure("Treeview",
                            foreground="blue",  # Foreground color of text
                            background="lightgray",  # Background color of rows
                            rowheight=30,  # Row height
                            coloumnwidth=30,
                            fieldbackground="lightgray",  # Background color of cells
                            font=("Arial", 12)  # Font for text
                            )

    tree.pack()

    add_row_button = ttk.Button(main_view, text="Add Row", command=lambda: add_data(tree))
    add_row_button.pack(pady=10)
    
'''
input methods -- 
    entry
    scanner
    voice
    
button - 
    adding product
    remove product
    submit button for adding manuval entries
'''