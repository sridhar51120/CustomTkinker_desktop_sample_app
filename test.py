# import math
# def create_product_cards(products, num_rows, num_columns):
#     for i, product in enumerate(products):
#         i = i + 1
#         print(i,product)
#         # # Create an instance of the Card class
#         # card = Card(
#         #     master=cards, card_fg_color="#2A8C55", card_width=200, card_height=60, card_pack_side="left")

#         # # Calculate row and column indices
#         # row_index =  num_columns
#         # col_index = num_columns

#         # # Display product image in the first column
#         # card.CardImage(image="delivered_icon.png", light_image="delivered_icon.png", dark_image="delivered_icon.png",
#         #                image_height=43, image_width=43, image_row=row_index, image_col=col_index, padx=(12, 5), pady=10, image_rowspan=2)

#         # # Display product details in the remaining columns
#         # card.CardLabel(label_text=f"Name: {product['name']}", label_color="black", label_font_family="Arial", label_font_size=12, label_row=row_index, label_col=col_index + 1, label_sticky="w", label_pady=(5, 0))
#         # card.CardLabel(label_text=f"Price: {product['price']}", label_color="green", label_font_family="Arial", label_font_size=10, label_row=row_index, label_col=col_index + 2, label_sticky="w", label_pady=(5, 0))
#         # card.CardLabel(label_text=f"Description: {product['description']}", label_color="blue", label_font_family="Arial", label_font_size=10, label_row=row_index, label_col=col_index + 3, label_sticky="w", label_pady=(5, 0))


# products_data = [
#     {"name": "Product 1", "price": "$19.99", "description": "Lorem ipsum..."},
#     {"name": "Product 2", "price": "$29.99", "description": "Lorem ipsum..."},
#     {"name": "Product 3", "price": "$39.99", "description": "Lorem ipsum..."},
#     {"name": "Product 4", "price": "$49.99", "description": "Lorem ipsum..."},
#     {"name": "Product 5", "price": "$59.99", "description": "Lorem ipsum..."},
#     {"name": "Product 6", "price": "$69.99", "description": "Lorem ipsum..."},
#     {"name": "Product 7", "price": "$79.99", "description": "Lorem ipsum..."},
#     {"name": "Product 8", "price": "$89.99", "description": "Lorem ipsum..."},
#     {"name": "Product 9", "price": "$99.99", "description": "Lorem ipsum..."},
#     {"name": "Product 10", "price": "$109.99", "description": "Lorem ipsum..."},
#     # Add more product details as needed
# ]
# num_columns=3
# num_rows = int(math.ceil(len(products_data)/num_columns))
# # # Create multiple instances of the Card class with a custom layout
# create_product_cards(products_data, num_rows, num_columns)

# # app.mainloop()

for i in range(10):
    for j in range(10):
        print(f"{i} => i, {j} => j")