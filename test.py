import tkinter as tk
from tkinter import ttk

def update_table(order_id, item_name, customer, address, status, quantity):
    tree.insert("", "end", values=(order_id, item_name, customer, address, status, quantity))

app = tk.Tk()
app.geometry("856x645")
app.resizable(0, 0)

columns = ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"]
tree = ttk.Treeview(app, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack()

# Take input values from console using input()
entry_order_id = input("Enter Order ID: ")
entry_item_name = input("Enter Item Name: ")
entry_customer = input("Enter Customer: ")
entry_address = input("Enter Address: ")
entry_status = input("Enter Status: ")
entry_quantity = input("Enter Quantity: ")

# Update the table with the input values
update_table(entry_order_id, entry_item_name, entry_customer, entry_address, entry_status, entry_quantity)

app.mainloop()
