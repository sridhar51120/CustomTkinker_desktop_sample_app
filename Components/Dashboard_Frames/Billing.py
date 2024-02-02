import tkinter as tk
from tkinter import ttk
from customtkinter import *
from CTkTable import CTkTable

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
    table_data = [
        ["Product ID", "Item Name", "Product Rate", "Total Count", "Price"],
        ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed'],
        ['6432', 'Laptop', 'Bob', '456 Elm St', 'Packing'],
        ['2180', 'Tablet', 'Crystal', '789 Oak St', 'Delivered'],
        ['5438', 'Headphones', 'John', '101 Pine St', 'Confirmed'],
        ['9144', 'Camera', 'David', '202 Cedar St', 'Processing'],
        ['7689', 'Printer', 'Alice', '303 Maple St', 'Cancelled'],
        ['1323', 'Smartwatch', 'Crystal', '404 Birch St', 'Shipping'],
        ['7391', 'Keyboard', 'John', '505 Redwood St', 'Cancelled',],
        ['4915', 'Monitor', 'Alice', '606 Fir St', 'Shipping'],
        ['5548', 'External Hard Drive', 'David', '707 Oak St', 'Delivered',],
        ['5485', 'Table Lamp', 'Crystal', '808 Pine St', 'Confirmed'],
        ['7764', 'Desk Chair', 'Bob', '909 Cedar St', 'Processing'],
        ['8252', 'Coffee Maker', 'John', '1010 Elm St', 'Confirmed'],
        ['2377', 'Blender', 'David', '1111 Redwood St', 'Shipping'],
        ['5287', 'Toaster', 'Alice', '1212 Maple St', 'Processing'],
        ['7739', 'Microwave', 'Crystal', '1313 Cedar St', 'Confirmed'],
        ['3129', 'Refrigerator', 'John', '1414 Oak St', 'Processing'],
        ['4789', 'Vacuum Cleaner', 'Bob', '1515 Pine St', 'Cancelled']
    ]
    
    table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=[
        "#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)
    # for i, l in enumerate(['9', 'r', 'B', 't', 'd']):
    #     table.add_row(i,l)

