from customtkinter import CTk, CTkLabel

class Label:
    def __init__(self, master, text, font_size, fg_color, relx, rely, anchor):
        self.master = master
        self.text = text
        self.font_size = font_size
        self.fg_color = fg_color
        self.relx = relx
        self.rely = rely
        self.anchor = anchor

        # Create a Label
        self.label = CTkLabel(
            master=self.master, text=self.text, font=(self.fg_color, self.font_size)
        )

        # Place the Label
        self.label.place(relx=self.relx, rely=self.rely, anchor=self.anchor)
        
    def update_text(self,new_text):
        self.label.configure(text=f"{new_text}")

    def change_font(self,new_font):
        '''
        ("Arial", 14, "bold")
        '''
        self.label.configure(font=new_font) 
        

    def change_color(self,fg):
        '''
        "blue"
        '''
        self.label.configure(fg_color=fg)

    def change_background(self,bg):
        '''
        "yellow"
        '''
        self.label.configure(bg_color=bg)

    def toggle_visibility(self):
        if self.label.winfo_ismapped():
            self.label.pack_forget()
        else:
            self.label.pack()
        
app = CTk()
app.geometry("500x400")

label = Label(
    master=app, text="Hello, CustomTkinter!", font_size=20, fg_color="#FFCC70",
    relx=0.5, rely=0.5, anchor="center"
)

label.update_text('New Text')
label.change_font(("Arial", 14, "bold"))
label.change_color('blue')
label.change_background('yellow')
label.toggle_visibility()

app.mainloop()
