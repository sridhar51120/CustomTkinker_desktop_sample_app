import tkinter as tk
from tkinter import ttk
from customtkinter import *

def update_table(tree, order_id, item_name, customer, address, status, quantity):
    tree.insert("", "end", values=(order_id, item_name, customer, address, status, quantity))

def add_row(tree):
    entry_order_id = input("Enter Order ID: ")
    entry_item_name = input("Enter Item Name: ")
    entry_customer = input("Enter Customer: ")
    entry_address = input("Enter Address: ")
    entry_status = input("Enter Status: ")
    entry_quantity = input("Enter Quantity: ")

    update_table(tree, entry_order_id, entry_item_name, entry_customer, entry_address, entry_status, entry_quantity)
    print("Row Completed")

def tab_billing(main_view):
    columns = ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"]
    tree = ttk.Treeview(main_view, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)

    tree.pack()

    add_row_button = ttk.Button(main_view, text="Add Row", command=lambda: add_row(tree))
    add_row_button.pack(pady=10)

