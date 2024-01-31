import json
import random
import string

# Function to generate random product data
def generate_product():
    product_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    product_name = 'Product ' + ''.join(random.choices(string.ascii_uppercase, k=5))
    product_price = round(random.uniform(10.0, 100.0), 2)
    return {'id': product_id, 'name': product_name, 'price': product_price}

# Generate 100 random products
products_list = [generate_product() for _ in range(100)]

# Create a JSON structure
json_data = {'products': products_list}

# Write the JSON data to a file
with open('products_data.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)
