from customtkinter import *
from CTkTable import CTkTable
from PIL import Image

app = CTk()
app.geometry("856x645")
app.resizable(0, 0)

set_appearance_mode("light")

sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55",
                         width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("G:/GITHUB/GUI/images/logo.png")
logo_img = CTkImage(dark_image=logo_img_data,
                    light_image=logo_img_data, size=(77.68, 85.42))

CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(
    pady=(38, 0), anchor="center")

analytics_img_data = Image.open("G:/GITHUB/GUI/images/analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data,
                         light_image=analytics_img_data)

CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=(
    "Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

package_img_data = Image.open("G:/GITHUB/GUI/images/package_icon.png")
package_img = CTkImage(dark_image=package_img_data,
                       light_image=package_img_data)
CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="#fff", font=("Arial Bold", 14),
          text_color="#2A8C55", hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

list_img_data = Image.open("G:/GITHUB/GUI/images/list_icon.png")
list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=(
    "Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

returns_img_data = Image.open("G:/GITHUB/GUI/images/returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data,
                       light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=(
    "Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

settings_img_data = Image.open("G:/GITHUB/GUI/images/settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data,
                        light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=(
    "Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

person_img_data = Image.open("G:/GITHUB/GUI/images/person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=(
    "Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

main_view = CTkFrame(master=app, fg_color="#fff",
                     width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

title_frame = CTkFrame(
    master=main_view, fg_color="transparent", height=20, width=100)
title_frame.pack(anchor="n", fill="x",  padx=27)
# title_frame.lable()

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
table_frame.pack(expand=True, fill="both", padx=27, pady=5)
table = CTkTable(master=table_frame, values=table_data, colors=[
                 "#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
table.pack(expand=True)

app.mainloop()
