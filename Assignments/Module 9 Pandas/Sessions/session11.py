import pandas as pd

# 1.Use pd.concat to combine two DataFrames representing January and February orders from a Swiggy-style food delivery app, stacking them row-wise to create a single DataFrame with all orders.

'''
jan_orders = pd.DataFrame({
    'order_id': [101, 102, 103],
    'customer': ['Rahul', 'Priya', 'Amit'],
    'amount': [450, 600, 350]
})

feb_orders = pd.DataFrame({
    'order_id': [104, 105, 106],
    'customer': ['Neha', 'Karan', 'Riya'],
    'amount': [700, 500, 800]
})

all_orders = pd.concat([jan_orders, feb_orders], ignore_index=True)

print(all_orders)
'''


# 2.Given two DataFrames — one with Flipkart product details and another with their respective ratings — use pd.concat to merge them column-wise so each product row includes its rating.

'''
products = pd.DataFrame({
    'product_id': [101, 102, 103, 104],
    'product_name': ['Laptop', 'Phone', 'Headphones', 'Smartwatch'],
    'price': [45000, 20000, 2500, 5000]
})

ratings = pd.DataFrame({
    'rating': [4.5, 4.2, 4.0, 4.3]
})

result = pd.concat([products, ratings], axis=1)

print(result)
'''


# 3.Create a DataFrame showing daily song streams for three users on Spotify for one week, then use the pivot function to reshape the data so each row is a user and each column is a day.

'''
data = pd.DataFrame({
    'user': ['Rahul', 'Rahul', 'Rahul', 'Priya', 'Priya', 'Priya',
             'Amit', 'Amit', 'Amit'],
    'day': ['Monday', 'Tuesday', 'Wednesday', 'Monday', 'Tuesday', 'Wednesday',
            'Monday', 'Tuesday', 'Wednesday'],
    'streams': [120, 150, 180, 200, 220, 190, 100, 130, 160]
})

result = data.pivot(index='user', columns='day', values='streams')

print(result)
'''

# 4.Given a DataFrame of Zomato restaurant orders (with columns: restaurant, month, total_amount), use pivot_table to calculate the average order amount per restaurant for each month.

'''
data = pd.DataFrame({
    'restaurant': ['Dominos', 'Dominos', 'KFC', 'KFC', 'Pizza Hut', 'Pizza Hut'],
    'month': ['January', 'February', 'January', 'February', 'January', 'February'],
    'total_amount': [500, 600, 450, 550, 700, 800]
})

result = data.pivot_table(
    index='restaurant',
    columns='month',
    values='total_amount',
    aggfunc='mean'
)

print(result)
'''


# 5.Download three monthly sales CSV files for a mock Myntra store (e.g., sales_jan.csv, sales_feb.csv, sales_mar.csv), then use pd.concat to combine them into one DataFrame and display the total sales per product.<br><br><em><strong>Hint:</strong> Use groupby on the product column after concatenation to sum sales.</em>
'''
jan = pd.read_csv('sales_jan.csv')
feb = pd.read_csv('sales_feb.csv')
mar = pd.read_csv('sales_mar.csv')

all_sales = pd.concat([jan, feb, mar], ignore_index=True)

total_sales = all_sales.groupby('product')['sales'].sum()

print(total_sales)
'''