from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
from Components.Card import *


def tab_sales(main_view):
    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    CTkLabel(master=title_frame, text="Sales", font=("Arial Black", 25),
             text_color="#2A8C55").pack(anchor="nw", side="left")

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(20, 0))

    CTkLabel(master=title_frame, text="Sales", font=("Arial Black", 15),
             text_color="#0000FF").pack(anchor="nw", side="left")
    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(10, 0))

    orders_metric = CTkFrame(master=metrics_frame,
                             fg_color="#2A8C55", width=200, height=100)
    orders_metric.grid_propagate(0)
    orders_metric.pack(side="left")
    logitics_img_data = Image.open("G:/GITHUB/GUI/images/1.png")
    logistics_img = CTkImage(light_image=logitics_img_data,
                             dark_image=logitics_img_data, size=(43, 43))

    CTkLabel(master=orders_metric, image=logistics_img, text="").grid(
        row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
    CTkLabel(master=orders_metric, text="1 Day sale", text_color="#fff",
             font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=orders_metric, text="123", text_color="#fff", font=(
        "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

    shipped_metric = CTkFrame(master=metrics_frame,
                              fg_color="#2A8C55", width=200, height=100)
    shipped_metric.grid_propagate(0)
    shipped_metric.pack(side="left", expand=True, anchor="center")
    shipping_img_data = Image.open("G:/GITHUB/GUI/images/7.png")
    shipping_img = CTkImage(light_image=shipping_img_data,
                            dark_image=shipping_img_data, size=(43, 43))
    CTkLabel(master=shipped_metric, image=shipping_img, text="").grid(
        row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
    CTkLabel(master=shipped_metric, text="7 Days sales", text_color="#fff",
             font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=shipped_metric, text="91", text_color="#fff", font=(
        "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

    delivered_metric = CTkFrame(
        master=metrics_frame, fg_color="#2A8C55", width=200, height=100)
    delivered_metric.grid_propagate(0)
    delivered_metric.pack(side="right",)
    delivered_img_data = Image.open("G:/GITHUB/GUI/images/3.jpg")
    delivered_img = CTkImage(light_image=delivered_img_data,
                             dark_image=delivered_img_data, size=(43, 43))
    CTkLabel(master=delivered_metric, image=delivered_img, text="").grid(
        row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
    CTkLabel(master=delivered_metric, text="30 Days sales", text_color="#fff",
             font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=delivered_metric, text="23", text_color="#fff", font=(
        "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

    # For Total number of bills
    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(20, 0))

    CTkLabel(master=title_frame, text="Total Numbers of Bills", font=("Arial Black", 15),
             text_color="#0000FF").pack(anchor="nw", side="left")
    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(10, 0))

    orders_metric = CTkFrame(master=metrics_frame,
                             fg_color="#2A8C55", width=200, height=100)
    orders_metric.grid_propagate(0)
    orders_metric.pack(side="left")
    logitics_img_data = Image.open("G:/GITHUB/GUI/images/1.png")
    logistics_img = CTkImage(light_image=logitics_img_data,
                             dark_image=logitics_img_data, size=(43, 43))

    CTkLabel(master=orders_metric, image=logistics_img, text="").grid(
        row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
    CTkLabel(master=orders_metric, text="1 Day Bill", text_color="#fff",
             font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=orders_metric, text="123", text_color="#fff", font=(
        "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

    shipped_metric = CTkFrame(master=metrics_frame,
                              fg_color="#2A8C55", width=200, height=100)
    shipped_metric.grid_propagate(0)
    shipped_metric.pack(side="left", expand=True, anchor="center")
    shipping_img_data = Image.open("G:/GITHUB/GUI/images/7.png")
    shipping_img = CTkImage(light_image=shipping_img_data,
                            dark_image=shipping_img_data, size=(43, 43))
    CTkLabel(master=shipped_metric, image=shipping_img, text="").grid(
        row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
    CTkLabel(master=shipped_metric, text="7 Days Bills", text_color="#fff",
             font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=shipped_metric, text="91", text_color="#fff", font=(
        "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

    delivered_metric = CTkFrame(
        master=metrics_frame, fg_color="#2A8C55", width=200, height=100)
    delivered_metric.grid_propagate(0)
    delivered_metric.pack(side="right",)
    delivered_img_data = Image.open("G:/GITHUB/GUI/images/3.jpg")
    delivered_img = CTkImage(light_image=delivered_img_data,
                             dark_image=delivered_img_data, size=(43, 43))
    CTkLabel(master=delivered_metric, image=delivered_img, text="").grid(
        row=0, column=0, rowspan=2, padx=(12, 5), pady=10)
    CTkLabel(master=delivered_metric, text="30 Days Bill", text_color="#fff",
             font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=delivered_metric, text="23", text_color="#fff", font=(
        "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

    # Total number of Products Sold
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
