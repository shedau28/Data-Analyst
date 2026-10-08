import pandas as pd

# 1.Download a dataset of IPL cricket matches (CSV) and use pandas to group the data by 'team' to find the total runs scored by each team. Display the result as a DataFrame.

'''
data = pd.DataFrame({
    'team': ['MI', 'CSK', 'RCB', 'MI', 'CSK', 'RCB', 'KKR', 'KKR'],
    'runs': [185, 210, 195, 170, 190, 205, 220, 180]
})

result = data.groupby('team', as_index=False)['runs'].sum()
result = result.rename(columns={'runs': 'total_runs'})

print(result)
'''


# 2.Given a DataFrame of Zomato food orders with columns ['city', 'restaurant', 'order_amount'], use groupby to calculate the average order_amount for each restaurant in each city using the agg() function.

'''
data = pd.DataFrame({
    'city': ['Delhi', 'Delhi', 'Mumbai', 'Mumbai', 'Pune', 'Pune'],
    'restaurant': ['Dominos', 'KFC', 'Dominos', 'KFC', 'Dominos', 'KFC'],
    'order_amount': [500, 600, 700, 800, 400, 500]
})

result = data.groupby(['city', 'restaurant']).agg(
    average_order_amount=('order_amount', 'mean')
).reset_index()

print(result)
'''

# 3.Take a Flipkart-style product sales DataFrame with columns ['category', 'region', 'sales', 'units_sold'], and apply multiple aggregations: for each (category, region) pair, calculate the total sales and the average units_sold using groupby and agg().

'''
data = pd.DataFrame({
    'category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Electronics', 'Clothing'],
    'region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'sales': [50000, 60000, 30000, 40000, 70000, 35000],
    'units_sold': [100, 120, 150, 180, 140, 160]
})

result = data.groupby(['category', 'region']).agg(
    total_sales=('sales', 'sum'),
    average_units_sold=('units_sold', 'mean')
).reset_index()

print(result)
'''


# 4.Refactor the code that groups a DataFrame by 'region' and sums 'revenue' so it also returns the maximum and minimum revenue per region in the same result.<br><br><em><strong>Hint:</strong> Use agg() with a dictionary to specify multiple aggregation functions for the 'revenue' column.</em>

'''
data = pd.DataFrame({
    'region': ['North', 'North', 'South', 'South', 'West', 'West'],
    'revenue': [50000, 70000, 45000, 60000, 80000, 55000]
})

result = data.groupby('region').agg({
    'revenue': ['sum', 'max', 'min']
})

print(result)
'''


# 5.Suppose you have a DataFrame of Spotify song streams with columns ['artist', 'genre', 'streams']. Use groupby and agg() to find both the total and average streams for each genre, then sort the result by total streams in descending order.<br><br><em><strong>Constraint:</strong> Your final DataFrame should have genres as the index and columns for total and average streams.</em>

'''
data = pd.DataFrame({
    'artist': ['Artist A', 'Artist B', 'Artist C', 'Artist D', 'Artist E', 'Artist F'],
    'genre': ['Pop', 'Rock', 'Pop', 'Hip-Hop', 'Rock', 'Hip-Hop'],
    'streams': [5000000, 3000000, 4000000, 2500000, 3500000, 2000000]
})

result = data.groupby('genre').agg(
    total_streams=('streams', 'sum'),
    average_streams=('streams', 'mean')
).sort_values('total_streams', ascending=False)

print(result)
'''