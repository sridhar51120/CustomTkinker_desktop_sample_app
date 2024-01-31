from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
from Components.Card import *


def tab_products(main_view):
    # TODO: Add the database connection and include the real time products
    products_data = [
        {"name": "Product 1", "price": "$19.99", "description": "Lorem ipsum..."},
        {"name": "Product 2", "price": "$29.99", "description": "Lorem ipsum..."},
        {"name": "Product 3", "price": "$39.99", "description": "Lorem ipsum..."},
        {"name": "Product 4", "price": "$49.99", "description": "Lorem ipsum..."},
        {"name": "Product 5", "price": "$59.99", "description": "Lorem ipsum..."},
        {"name": "Product 6", "price": "$69.99", "description": "Lorem ipsum..."},
        {"name": "Product 7", "price": "$79.99", "description": "Lorem ipsum..."},
        {"name": "Product 8", "price": "$89.99", "description": "Lorem ipsum..."},
        {"name": "Product 9", "price": "$99.99", "description": "Lorem ipsum..."},
        {"name": "Product 10", "price": "$109.99", "description": "Lorem ipsum..."},
    ]

    for row, product in enumerate(products_data):
        for col in range(3):
            card = Card(
                master=main_view, card_fg_color="#2A8C55", card_width=200, card_height=60, card_pack_side="right",
                row=row, col=col
            )
            image_path = "delivered_icon.png"

            image_row = row * 2
            image_col = col * 2

            card.CardImage(
                image=image_path, light_image=image_path, dark_image=image_path,
                image_height=43, image_width=43, image_row=image_row, image_col=image_col,
                padx=(12, 5), pady=10, image_rowspan=2
            )
            
            card.CardLabel(
                label_text="Delivered", label_color="#fff", label_font_family="Arial Black", label_font_size=15,
                label_row=image_row + 1, label_col=image_col, label_sticky="sw", label_padx=None,
                label_pady=None, label_row_span=None, label_col_span=None
            )

            card.CardLabel(
                label_text=f"{product['name']}", label_color="#fff", label_font_family="Arial Black",
                label_font_size=15, label_row=image_row + 1, label_col=image_col + 1,
                label_sticky="nw", label_pady=(0, 10), label_content_side="left"
            )
            

