from customtkinter import *
from PIL import Image

class Button:
    def __init__(self, master, text, corner_radius, fg_color, hover_color, border_color, border_width, image, relx, rely, anchor):
        self.master = master
        self.text = text
        self.corner_radius = corner_radius
        self.fg_color = fg_color
        self.hover_color = hover_color
        self.border_color = border_color
        self.border_width = border_width  
        self.image = image
        self.relx = relx
        self.rely = rely
        self.anchor = anchor
        self.btn = CTkButton(master=self.master, text=self.text, corner_radius=self.corner_radius, fg_color=self.fg_color,
                hover_color=self.hover_color, border_color=self.border_color,
                border_width=self.border_width, image=self.image)
        self.btn.place(relx=self.relx, rely=self.rely, anchor=self.anchor)
        self.parameter_list = ['Onclick', 'invoke', 'flash', 'disable', 'change_button_text', 'get_button_text', 'bound', 'unbound', 'get_current_state', 'check_disable_state']
        
    def execute_command(self, parameter, user_function=None, new_text_button=None):
        try:
            if parameter not in self.parameter_list:
                raise ValueError(f"Parameter Not Found: {parameter}")
            else:
                if parameter == 'Onclick':
                    # Bind the function without calling it
                    self.btn.bind("<Button-1>", lambda event: user_function())
                    
                elif parameter == 'invoke':
                    if callable(user_function):
                        user_function()
                        
                elif parameter == 'flash':
                    self.btn.flash()
                    
                elif parameter == 'disable':
                    self.btn.state(["disabled"])
                    
                elif parameter == 'change_button_text':
                    if new_text_button is not None:
                        self.btn.config(text=new_text_button)
                    elif new_text_button is None:
                        self.btn.config(text="Default Text")
                        
                elif parameter == 'get_button_text':
                    text_value = self.btn.cget("text")
                    return text_value
                
                elif parameter == 'bound':
                    self.btn.bind("<Button-1>", lambda event: print("Button is bound"))

                elif parameter == 'unbound':
                    self.btn.unbind("<Button-1>")

                elif parameter == 'get_current_state':
                    current_state = self.btn.cget("state")
                    return current_state

                elif parameter == 'check_disable_state':
                    is_disabled = "disabled" in self.btn.state()
                    return is_disabled

        except ValueError as e:
            print(e)

def hello():
    print("3.14")

app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")
btn = Button(master=app, text="Click Me", corner_radius=32, fg_color="#4158D0", 
                hover_color="#C850C0", border_color="#FFCC70", 
                border_width=2, image=CTkImage(dark_image=Image.open("message_icon.png")), relx=0.5, rely=0.5, anchor="center")


btn.execute_command('Onclick', user_function=hello)
app.mainloop()
