from customtkinter import *
from PIL import Image
from CTkTable import CTkTable


class ScrollableFrame:
    def __init__(self, master, frame_fg_color, frame_expand, frame_fill, frame_padx, frame_pady):
        self.master = master
        self.frame_fg_color = frame_fg_color
        self.frame_expand = frame_expand
        self.frame_fill = frame_fill
        self.frame_padx = frame_padx
        self.frame_pady = frame_pady

        # Create Scorralable Frame
        self.scrollable_frame = CTkScrollableFrame(
            master=self.master, fg_color=self.frame_fg_color)
        self.scrollable_frame.pack(
            expand=self.frame_expand, fill=self.frame_fill, padx=self.frame_padx, pady=self.frame_pady)

    def validate_table_data(self, data):
        if not isinstance(data, list):
            return False, "Invalid data format. Must be a list."
        num_columns = len(data[0])
        for row in data[1:]:
            if not isinstance(row, list) or len(row) != num_columns:
                return False, "Invalid data format. Rows must be lists with the same number of columns."
        return True

    def create_table(self, values, colors, header_color, hover_color, edit_row=None, edit_text_color=None, edit_hover_color=None, table_expand=None):
        if self.validate_table_data(values):
            print("Table Row with Coloumn is validated")
            table = CTkTable(master=self.scrollable_frame, values=table_data, colors=[
                "#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
            table.edit_row(edit_row, text_color=edit_text_color,
                           hover_color=edit_hover_color)
            table.pack(expand=True)
        else:
            raise Exception("table row and coloumn mismatch values")

    def lable(self, label_text, font_family, font_size, text_color, bg_color, row, col, ancher, expand, padx=None, pady=None):

        label = CTkLabel(master=self.scrollable_frame, text=f"{label_text}", font=(
            f"{font_family}", font_size), text_color=text_color, bg_color=bg_color)
        label.pack(anchor=ancher, expand=expand, padx=padx, pady=pady)

    def entry(self, placeholder_text):
        pass

    def btn(self, text, corner_radius, fg_color, hover_color, border_color, border_width,  relx, rely, anchor,command, image=None,user_function=None):
        command_list = ['Onclick', 'invoke', 'flash', 'disable', 'change_button_text', 'get_button_text', 'bound', 'unbound', 'get_current_state', 'check_disable_state']
        btn = CTkButton(master=self.scrollable_frame, text=text, corner_radius=corner_radius, fg_color=fg_color,
                        hover_color=hover_color, border_color=border_color,
                        border_width=border_width, image=image)
        btn.place(relx=relx, rely=rely, anchor=anchor)
        try:
            if command not in command_list:
                raise ValueError(f"command Not Found: {command}")
            else:
                if command == 'Onclick':
                    # Bind the function without calling it
                    btn.bind("<Button-1>", lambda event: user_function())
                    
                elif command == 'invoke':
                    if callable(user_function):
                        user_function()
                        
                elif command == 'flash':
                    btn.flash()
                    
                elif command == 'disable':
                    btn.state(["disabled"])
                    
                elif command == 'change_button_text':
                    if new_text_button is not None:
                        btn.config(text=new_text_button)
                    elif new_text_button is None:
                        btn.config(text="Default Text")
                        
                elif command == 'get_button_text':
                    text_value = btn.cget("text")
                    return text_value
                
                elif command == 'bound':
                    btn.bind("<Button-1>", lambda event: print("Button is bound"))

                elif command == 'unbound':
                    btn.unbind("<Button-1>")

                elif command == 'get_current_state':
                    current_state = btn.cget("state")
                    return current_state

                elif command == 'check_disable_state':
                    is_disabled = "disabled" in btn.state()
                    return is_disabled
                
        except ValueError as e:
            print(e)


# entry = CTkEntry(master=frame, placeholder_text="Type something...")
# btn = CTkButton(master=frame, text="Submit")

# label.pack(anchor="s", expand=True, pady=10, padx=30)
# entry.pack(anchor="s", expand=True, pady=10, padx=30)
# btn.pack(anchor="n", expand=True, padx=30, pady=20)


# Test
app = CTk()
app.geometry("500x400")

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

table_frame = ScrollableFrame(master=app, frame_fg_color="transparent",
                              frame_expand=True, frame_fill="both", frame_padx=27, frame_pady=21)

table_frame.create_table(values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55",
                         hover_color="#B4B4B4", edit_row=0, edit_text_color="#fff", edit_hover_color="#2A8C55", table_expand=True)

def hello():
    print("3.14")

btn = table_frame.btn(text="Click Me", corner_radius=32, fg_color="#4158D0", 
                hover_color="#C850C0", border_color="#FFCC70", 
                border_width=2, image=CTkImage(dark_image=Image.open("message_icon.png")), relx=0.5, rely=0.5, anchor="center",command='Onclick', user_function=hello)

app.mainloop()
