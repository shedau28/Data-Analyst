import numpy as np

# Read CSV
data = np.genfromtxt(
    "numpy_dataset.csv",
    delimiter=",",
    dtype=None,
    names=True,
    encoding="utf-8"
)
# print(data)

print(data.dtype.names)

# Base Price column
base_prices = data['Base_Price_₹']
# print(base_prices)

# Index of cheapest product
min_index = np.argmin(base_prices)
# print(min_index)

# Product ID
cheapest_product = data["Product_ID"][min_index]
# print(cheapest_product)

# Cheapest price
cheapest_price = base_prices[min_index]
# print(cheapest_price)

print(data.dtype.names)
# Find costly product

costly_prod_index = np.argmax(data['Base_Price_₹'])

costly_prod_name = data['Product_ID'][costly_prod_index]
costly_prod_price = data["Base_Price_₹"][costly_prod_index]

# print(costly_prod_name)
# print(costly_prod_price)

# print(np.min(data["Base_Price_₹"]))
# print(np.max(data["Base_Price_₹"]))

# result = data[data["Base_Price_₹"] > 700]
result = data[data["Base_Price_₹"] > 700]
# print(result)
