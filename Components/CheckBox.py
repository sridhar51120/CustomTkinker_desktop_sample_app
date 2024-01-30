from customtkinter import CTk, CTkCheckBox
import tkinter as tk

class CheckBox:
    def __init__(self, master, text, fg_color, checkbox_height, checkbox_width, corner_radius, relx, rely, anchor):
        self.master = master
        self.text = text
        self.fg_color = fg_color
        self.checkbox_height = checkbox_height
        self.checkbox_width = checkbox_width
        self.corner_radius = corner_radius
        self.relx = relx
        self.rely = rely
        self.anchor = anchor
        self.checkbox_var = tk.BooleanVar()

        # Create a CheckBox
        self.checkbox = CTkCheckBox(
            master=self.master, text=self.text, fg_color=self.fg_color, checkbox_height=self.checkbox_height,
            checkbox_width=self.checkbox_width, corner_radius=self.corner_radius,variable=self.checkbox_var
        )

        # Place the CheckBox
        self.checkbox.place(relx=self.relx, rely=self.rely, anchor=self.anchor)

    def execute_command(self, event, new_text=None):
        try:
            if event not in ['select', 'deselect', 'invoke', 'cget', 'config', 'state', 'setValue','isSelected']:
                raise ValueError(f"Event Not Found: {event}")
            else:
                if event == 'select':
                    self.checkbox.select()
                    
                elif event == 'deselect':
                    self.checkbox.deselect()
                    
                elif event == 'invoke':
                    self.checkbox.invoke()
                    
                elif event == 'cget':
                    return self.checkbox.instate(["selected"])  # Use instate to check if selected
                
                elif event == 'config':
                    if new_text is not None:
                        self.checkbox.configure(text=new_text)
                    else:
                        self.checkbox.configure(text="New Label")
                        
                elif event == 'state':
                    self.checkbox._state(["selected"])  # Use instate to check if not disabled
                
                elif event == 'isSelected':
                    # Retrieve the value of the checkbox variable (0 for unchecked, 1 for checked)
                    selected_value = self.checkbox.get()
                    # return selected_value
                    if selected_value:
                        print("Checkbox is selected!")
                    else:
                        print("Checkbox is unselected.")
                
                elif event == 'setValue':
                    value = self.checkbox.cget("variable").get()
                    self.checkbox.cget("variable").set(1)
                    
                else:
                    return False

        except ValueError as e:
            print(e)

def hello():
    print("3.14")

app = CTk()
app.geometry("500x400")

checkbox = CheckBox(
    master=app, text="Option", fg_color="#C850C0", checkbox_height=30,
    checkbox_width=30, corner_radius=36, relx=0.5, rely=0.5, anchor="center"
)
data = checkbox.execute_command('setValue')
print(data)

app.mainloop()
