from customtkinter import *
from PIL import Image

class Card:
    def __init__(self, master, card_fg_color, card_width, card_height, card_pack_side, row, col):
        self.master = master
        self.card_fg_color = card_fg_color
        self.card_width = card_width
        self.card_height = card_height
        self.card_pack_side = card_pack_side

        self.frame = CTkFrame(master=self.master, fg_color=self.card_fg_color,
                              width=self.card_width, height=self.card_height)
        self.frame.pack(side=self.card_pack_side)
        self.row = row  
        self.col = col
        self.frame.grid(row=row, column=col, padx=5, pady=5)

    def CardImage(self, image, light_image, dark_image, image_height, image_width, image_row, image_col, padx=None, pady=None, image_rowspan=None, image_colspan=None):
        image = Image.open(image)
        card_image = CTkImage(light_image=image, dark_image=image, size=(
            int(image_height), int(image_width)))
        CTkLabel(master=self.frame, image=card_image, text="").grid(
            row=image_row, column=image_col, rowspan=image_rowspan, padx=padx, pady=pady, columnspan=image_colspan)

    def CardLabel(self, label_text, label_color, label_font_family, label_font_size, label_row, label_col, label_sticky, label_padx=None, label_pady=None, label_row_span=None, label_col_span=None, label_content_side=None):
        CTkLabel(master=self.frame, text=label_text, text_color=f"{label_color}", font=(f"{label_font_family}", label_font_size), justify=label_content_side).grid(
            row=label_row, column=label_col, sticky=label_sticky, pady=label_pady, padx=label_padx, rowspan=label_row_span, columnspan=label_col_span)
