import tkinter as tk
from tkinter import ttk

def remove_row():
    selected_item = tree.selection()  # Get the selected item
    if selected_item:
        tree.delete(selected_item)  # Delete the selected item

# Create the main window
root = tk.Tk()
root.title("Remove Row Example")

# Create a Treeview
tree = ttk.Treeview(root, columns=('Column1', 'Column2', 'Column3'), show='headings')

# Add some sample data
data = [
    ("Value1", "Value2", "Value3"),
    ("Value4", "Value5", "Value6"),
    ("Value7", "Value8", "Value9"),
]

for row in data:
    tree.insert("", "end", values=row)

# Add headers
for col in ('Column1', 'Column2', 'Column3'):
    tree.heading(col, text=col)

# Add the Treeview to the window
tree.pack(pady=10)

# Button to remove the selected row
remove_button = tk.Button(root, text="Remove Selected Row", command=remove_row)
remove_button.pack(pady=10)

# Start the main loop
root.mainloop()
