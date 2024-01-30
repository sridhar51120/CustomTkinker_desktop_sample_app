# from customtkinter import *
# from CTkTable import CTkTable

# app = CTk()
# app.geometry("500x400")

# table_data = [
#     ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
#     ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed', '8'],
#     ['6432', 'Laptop', 'Bob', '456 Elm St', 'Packing', '5'],
#     ['2180', 'Tablet', 'Crystal', '789 Oak St', 'Delivered', '1'],
#     ['5438', 'Headphones', 'John', '101 Pine St', 'Confirmed', '9'],
#     ['9144', 'Camera', 'David', '202 Cedar St', 'Processing', '2'],
#     ['7689', 'Printer', 'Alice', '303 Maple St', 'Cancelled', '2'],
#     ['1323', 'Smartwatch', 'Crystal', '404 Birch St', 'Shipping', '6'],
#     ['7391', 'Keyboard', 'John', '505 Redwood St', 'Cancelled', '10'],
#     ['4915', 'Monitor', 'Alice', '606 Fir St', 'Shipping', '6'],
#     ['5548', 'External Hard Drive', 'David', '707 Oak St', 'Delivered', '10'],
#     ['5485', 'Table Lamp', 'Crystal', '808 Pine St', 'Confirmed', '4'],
#     ['7764', 'Desk Chair', 'Bob', '909 Cedar St', 'Processing', '9'],
#     ['8252', 'Coffee Maker', 'John', '1010 Elm St', 'Confirmed', '6'],
#     ['2377', 'Blender', 'David', '1111 Redwood St', 'Shipping', '2'],
#     ['5287', 'Toaster', 'Alice', '1212 Maple St', 'Processing', '1'],
#     ['7739', 'Microwave', 'Crystal', '1313 Cedar St', 'Confirmed', '8'],
#     ['3129', 'Refrigerator', 'John', '1414 Oak St', 'Processing', '5'],
#     ['4789', 'Vacuum Cleaner', 'Bob', '1515 Pine St', 'Cancelled', '10']
# ]

# table_frame = CTkScrollableFrame(master=app, fg_color="transparent")
# table_frame.pack(expand=True, fill="both", padx=27, pady=21)
# table = CTkTable(master=table_frame, values=table_data, colors=[
#                  "#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
# table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
# table.pack(expand=True)

# app.mainloop()
# def Hello(value):
#     print(d)
    
# Hello(value="hek")

# ls = []
# i = 0
# while True:
#     val = input()
#     if val == "stop":
#         break
#     else:
#         ls.append(val)
#         i = i + 1
#         print(f"{i} ith iterative ",ls)
        
        
# import tkinter as tk

# # Replace this with your actual product list data
# product_list = [
#     {"title": "Product A", "description": "Description A"},
#     {"title": "Product B", "description": "Description B"},
#     {"title": "Product C", "description": "Description C"},
#     {"title": "Product D", "description": "Description D"},
#     {"title": "Product E", "description": "Description E"},
#     {"title": "Product F", "description": "Description F"},
#     # Add more products as needed
# ]

# def create_product_widgets():
#     for i, product in enumerate(product_list):
#         # Title Label
#         title_label = tk.Label(root, text=product['title'], font=('Helvetica', 12, 'bold'), fg='blue')
#         title_label.grid(row=i//3, column=i%3, pady=5)

#         # Description Label
#         description_label = tk.Label(root, text=product['description'], font=('Helvetica', 10), wraplength=150, justify='center')
#         description_label.grid(row=i//3 + 1, column=i%3, pady=5)

# # Create the Tkinter window
# root = tk.Tk()
# root.title("Product List")

# # Call the function to create product widgets
# create_product_widgets()

# # Run the Tkinter event loop
# root.mainloop()

import barcode
from barcode.writer import ImageWriter
import requests



def get_product_details_from_api(barcode_data):
    """
    Fetch product details from the Open Food Facts API based on the barcode.
    """
    api_url = f'https://world.openfoodfacts.org/api/v0/product/{barcode_data}.json'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        product_data = response.json()
        return product_data
    else:
        return None

if __name__ == "__main__":
    # Example barcode data
    barcode_data = "1234567890123"
    
    # Generate barcode image

    # Get product details from the Open Food Facts API
    product_details = get_product_details_from_api(barcode_data)
    
    if product_details:
        print("Product Details:")
        print(f"Name: {product_details['product']['product_name']}")
        print(f"Brand: {product_details['product']['brands']}")
        print(f"Ingredients: {product_details['product']['ingredients_text']}")
    else:
        print("Product details not found.")
