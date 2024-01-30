from customtkinter import *
from PIL import Image

class Card:
    def __init__(self, master, card_fg_color, card_width, card_height, card_pack_side):
        self.master = master
        self.card_fg_color = card_fg_color
        self.card_width = card_width
        self.card_height = card_height
        self.card_pack_side = card_pack_side

        self.frame = CTkFrame(master=self.master, fg_color=self.card_fg_color,
                              width=self.card_width, height=self.card_height)
        self.frame.grid_propagate(0)
        self.frame.pack(side=self.card_pack_side)

    def CardImage(self, image, light_image, dark_image, image_height, image_width, image_row, image_col, padx=None, pady=None, image_rowspan=None, image_colspan=None):
        image = Image.open(image)
        card_image = CTkImage(light_image=image, dark_image=image, size=(
            int(image_height), int(image_width)))
        CTkLabel(master=self.frame, image=card_image, text="").grid(
            row=image_row, column=image_col, rowspan=image_rowspan, padx=padx, pady=pady, columnspan=image_colspan)

    def CardLabel(self, label_text, label_color, label_font_family, label_font_size, label_row, label_col, label_sticky, label_padx=None, label_pady=None, label_row_span=None, label_col_span=None, label_content_side=None):
        CTkLabel(master=self.frame, text=label_text, text_color=f"{label_color}", font=(f"{label_font_family}", label_font_size), justify=label_content_side).grid(
            row=label_row, column=label_col, sticky=label_sticky, pady=label_pady, padx=label_padx, rowspan=label_row_span, columnspan=label_col_span)


# Test Code

app = CTk()
app.geometry("500x400")

card = Card(
    master=app, card_fg_color="#2A8C55", card_width=200, card_height=60, card_pack_side="right")

card.CardImage(image="delivered_icon.png", light_image="delivered_icon.png", dark_image="delivered_icon.png",
               image_height=43, image_width=43, image_row=0, image_col=0, padx=(12, 5), pady=10, image_rowspan=2)

card.CardLabel(label_text="Delivered", label_color="#fff", label_font_family="Arial Black", label_font_size=15, label_row=0,
               label_col=1, label_sticky="sw", label_padx=None, label_pady=None, label_row_span=None, label_col_span=None)

card.CardLabel(label_text="23", label_color="#fff", label_font_family="Arial Black", label_font_size=15,
               label_row=1, label_col=1, label_sticky="nw", label_pady=(0, 10), label_content_side="left")

app.mainloop()
