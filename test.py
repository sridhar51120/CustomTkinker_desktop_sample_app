import tkinter as tk
from tkinter import ttk

def update_table():
    order_id = entry_order_id.get()
    item_name = entry_item_name.get()
    customer = entry_customer.get()
    address = entry_address.get()
    status = entry_status.get()
    quantity = entry_quantity.get()

    # Insert new row into the treeview
    tree.insert("", "end", values=(order_id, item_name, customer, address, status, quantity))

app = tk.Tk()
app.geometry("856x645")
app.resizable(0, 0)

# Entry widgets for user input
entry_order_id = ttk.Entry(app)
entry_item_name = ttk.Entry(app)
entry_customer = ttk.Entry(app)
entry_address = ttk.Entry(app)
entry_status = ttk.Entry(app)
entry_quantity = ttk.Entry(app)

# Button to update the table with user input
update_button = ttk.Button(app, text="Add Row", command=update_table)

# Create the initial table using ttk.Treeview
columns = ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"]
tree = ttk.Treeview(app, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack()

# Pack entry widgets and button
entry_order_id.pack(pady=5)
entry_item_name.pack(pady=5)
entry_customer.pack(pady=5)
entry_address.pack(pady=5)
entry_status.pack(pady=5)
entry_quantity.pack(pady=5)
update_button.pack(pady=10)

app.mainloop()
