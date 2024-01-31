from customtkinter import *
from CTkTable import CTkTable
from PIL import Image

def tab_dashboard(main_view):
    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    CTkLabel(master=title_frame, text="Orders", font=("Arial Black", 25),
            text_color="#2A8C55").pack(anchor="nw", side="left")

    CTkButton(master=title_frame, text="+ New Order",  font=("Arial Black", 15), text_color="#fff",
            fg_color="#2A8C55", hover_color="#207244").pack(anchor="ne", side="right")

    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

    orders_metric = CTkFrame(master=metrics_frame,
                            fg_color="#2A8C55", width=200, height=60)
    orders_metric.grid_propagate(0)
    orders_metric.pack(side="left")
    logitics_img_data = Image.open("G:/GITHUB/GUI/images/logistics_icon.png")
    logistics_img = CTkImage(light_image=logitics_img_data,
                            dark_image=logitics_img_data, size=(43, 43))

    CTkLabel(master=orders_metric, image=logistics_img, text="").grid(
        row=0, column=0, rowspan=2, padx=(12, 5), pady=10)

    CTkLabel(master=orders_metric, text="Orders", text_color="#fff",
            font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=orders_metric, text="123", text_color="#fff", font=(
        "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))


    shipped_metric = CTkFrame(master=metrics_frame,
                            fg_color="#2A8C55", width=200, height=60)
    shipped_metric.grid_propagate(0)
    shipped_metric.pack(side="left", expand=True, anchor="center")
    shipping_img_data = Image.open("G:/GITHUB/GUI/images/shipping_icon.png")
    shipping_img = CTkImage(light_image=shipping_img_data,
                            dark_image=shipping_img_data, size=(43, 43))
    CTkLabel(master=shipped_metric, image=shipping_img, text="").grid(
        row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
    CTkLabel(master=shipped_metric, text="Shipping", text_color="#fff",
            font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=shipped_metric, text="91", text_color="#fff", font=(
        "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

    delivered_metric = CTkFrame(
        master=metrics_frame, fg_color="#2A8C55", width=200, height=60)
    delivered_metric.grid_propagate(0)
    delivered_metric.pack(side="right",)
    delivered_img_data = Image.open("G:/GITHUB/GUI/images/delivered_icon.png")
    delivered_img = CTkImage(light_image=delivered_img_data,
                            dark_image=delivered_img_data, size=(43, 43))
    CTkLabel(master=delivered_metric, image=delivered_img, text="").grid(
        row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
    CTkLabel(master=delivered_metric, text="Delivered", text_color="#fff",
            font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=delivered_metric, text="23", text_color="#fff", font=(
        "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

    search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(45, 0), padx=27)

    CTkEntry(master=search_container, width=305, placeholder_text="Search Order",
            border_color="#2A8C55", border_width=2).pack(side="left", padx=(13, 0), pady=15)

    CTkComboBox(master=search_container, width=125, values=["Date", "Most Recent Order", "Least Recent Order"], button_color="#2A8C55", border_color="#2A8C55", border_width=2,
                button_hover_color="#207244", dropdown_hover_color="#207244", dropdown_fg_color="#2A8C55", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
    CTkComboBox(master=search_container, width=125, values=["Status", "Processing", "Confirmed", "Packing", "Shipping", "Delivered", "Cancelled"], button_color="#2A8C55", border_color="#2A8C55",
                border_width=2, button_hover_color="#207244", dropdown_hover_color="#207244", dropdown_fg_color="#2A8C55", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

    table_data = [
        ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
        ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed', '8'],
        ['6432', 'Laptop', 'Bob', '456 Elm St', 'Packing', '5'],
        ['2180', 'Tablet', 'Crystal', '789 Oak St', 'Delivered', '1'],
        ['5438', 'Headphones', 'John', '101 Pine St', 'Confirmed', '9'],
        ['9144', 'Camera', 'David', '202 Cedar St', 'Processing', '2'],
        ['7689', 'Printer', 'Alice', '303 Maple St', 'Cancelled', '2'],
        ['1323', 'Smartwatch', 'Crystal', '404 Birch St', 'Shipping', '6'],
        ['7391', 'Keyboard', 'John', '505 Redwood St', 'Cancelled', '10'],
        ['4915', 'Monitor', 'Alice', '606 Fir St', 'Shipping', '6'],
        ['5548', 'External Hard Drive', 'David', '707 Oak St', 'Delivered', '10'],
        ['5485', 'Table Lamp', 'Crystal', '808 Pine St', 'Confirmed', '4'],
        ['7764', 'Desk Chair', 'Bob', '909 Cedar St', 'Processing', '9'],
        ['8252', 'Coffee Maker', 'John', '1010 Elm St', 'Confirmed', '6'],
        ['2377', 'Blender', 'David', '1111 Redwood St', 'Shipping', '2'],
        ['5287', 'Toaster', 'Alice', '1212 Maple St', 'Processing', '1'],
        ['7739', 'Microwave', 'Crystal', '1313 Cedar St', 'Confirmed', '8'],
        ['3129', 'Refrigerator', 'John', '1414 Oak St', 'Processing', '5'],
        ['4789', 'Vacuum Cleaner', 'Bob', '1515 Pine St', 'Cancelled', '10']
    ]

    table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=[
                    "#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)
