import pandas as pd

# 1.Download a sample Flipkart-style product sales CSV with columns: ProductName, Price, Qty. Using pandas, add a new column called 'TotalValue' that multiplies Price and Qty for each row, then display the updated DataFrame.
'''
data = pd.DataFrame({
    'ProductName': ['Laptop', 'Smartphone', 'Headphones', 'Smartwatch', 'Keyboard'],
    'Price': [45000, 20000, 2500, 5000, 1500],
    'Qty': [2, 3, 5, 2, 4]
})

data['TotalValue'] = data['Price'] * data['Qty']

print(data)
'''


# 2.Given a DataFrame of food items with columns: Item, Price, and Qty, use the apply() function with a lambda to create a new column 'DiscountedPrice' that applies a 10% discount to the Price for each item.
'''
data = pd.DataFrame({
    'Item': ['Pizza', 'Burger', 'Biryani', 'Pasta', 'Sandwich'],
    'Price': [300, 200, 250, 220, 150],
    'Qty': [2, 3, 1, 2, 4]
})

data['DiscountedPrice'] = data['Price'].apply(lambda x: x * 0.90)

print(data)
'''

# 3.You have a DataFrame of Instagram posts with columns: PostID, Likes, and Comments. Use applymap() to convert all numeric values in the Likes and Comments columns to strings formatted as '1.5K', '2M', etc., similar to how Instagram displays large numbers.<br><br><em><strong>Hint:</strong> Write a helper function that takes a number and returns the formatted string, then use applymap() on the relevant columns.</em>
'''
data = pd.DataFrame({
    'PostID': [101, 102, 103, 104],
    'Likes': [1500, 2500000, 850000, 12000000],
    'Comments': [120, 4500, 1800, 250000]
})

def format_number(num):
    if num >= 1000000:
        return f'{num / 1000000:.1f}M'
    elif num >= 1000:
        return f'{num / 1000:.1f}K'
    else:
        return str(num)

data[['Likes', 'Comments']] = data[['Likes', 'Comments']].applymap(format_number)

print(data)'''

# 4.Given a DataFrame of Zomato restaurant orders with columns: Restaurant, Price, Qty, and DeliveryCharge, use a lambda function with apply() to add a column 'FinalAmount' that calculates the total amount for each order as (Price * Qty) + DeliveryCharge.

'''
data = pd.DataFrame({
    'Restaurant': ['Dominos', 'KFC', 'McDonalds', 'Pizza Hut', 'Subway'],
    'Price': [300, 250, 200, 350, 180],
    'Qty': [2, 3, 2, 1, 4],
    'DeliveryCharge': [40, 30, 25, 50, 20]
})

data['FinalAmount'] = data.apply(
    lambda row: (row['Price'] * row['Qty']) + row['DeliveryCharge'],
    axis=1
)

print(data)
'''


# 5.Use ChatGPT to generate a pandas code snippet that adds a column 'GST' to a DataFrame of Myntra orders, where GST is calculated as 5% of (Price * Qty). Paste the AI-generated code, run it, and write 2 lines about what you learned from the AI's explanation.

'''
data = pd.DataFrame({
    'Product': ['T-Shirt', 'Jeans', 'Shoes', 'Jacket'],
    'Price': [999, 1999, 2499, 2999],
    'Qty': [2, 1, 1, 2]
})

data['GST'] = (data['Price'] * data['Qty']) * 0.05

print(data)
'''

