import pandas as pd


# 1.Create two DataFrames: one called users with columns user_id, username, and city (add at least 5 rows), and another called orders with columns order_id, user_id, and order_amount (add at least 7 rows). Merge them using pd.merge() to show only users who have placed an order (inner join).

'''
users = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'username': ['Rahul', 'Priya', 'Amit', 'Neha', 'Karan'],
    'city': ['Delhi', 'Mumbai', 'Ahmedabad', 'Pune', 'Jaipur']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106, 107],
    'user_id': [1, 2, 1, 3, 2, 5, 3],
    'order_amount': [500, 750, 300, 900, 450, 650, 1200]
})

result = pd.merge(users, orders, on='user_id', how='inner')

print(result)
'''


# 2.Using the same users and orders DataFrames, perform a left join to display all users along with their orders. If a user has not placed any orders, show NaN for order_id and order_amount.<br><br><em><strong>Hint:</strong> Use the how='left' parameter in pd.merge().</em>

'''
result = pd.merge(users, orders, on='user_id', how='left')

print(result)

'''

# 3.Imagine you have two DataFrames: restaurants (restaurant_id, name, city) and zomato_reviews (review_id, restaurant_id, rating, reviewer_city). Merge them using an outer join on restaurant_id to show all restaurants and all reviews, even if some restaurants have no reviews or some reviews are for restaurants not in your list.

'''
restaurants = pd.DataFrame({
    'restaurant_id': [1, 2, 3, 4],
    'name': ['Dominos', 'KFC', 'Haldirams', 'Pizza Hut'],
    'city': ['Delhi', 'Mumbai', 'Ahmedabad', 'Pune']
})

zomato_reviews = pd.DataFrame({
    'review_id': [101, 102, 103, 104],
    'restaurant_id': [1, 2, 5, 3],
    'rating': [4.5, 4.0, 3.5, 4.8],
    'reviewer_city': ['Delhi', 'Mumbai', 'Jaipur', 'Ahmedabad']
})

result = pd.merge(restaurants, zomato_reviews, on='restaurant_id', how='outer')

print(result)
'''


# 4.Create two DataFrames: playlists (playlist_id, user_id, genre) and user_profiles (user_id, username, city). Merge them using pd.merge() on both user_id and city to get playlists where the playlist owner's city matches the user profile city.

'''
playlists = pd.DataFrame({
    'playlist_id': [101, 102, 103, 104, 105],
    'user_id': [1, 2, 3, 4, 5],
    'genre': ['Pop', 'Rock', 'Hip-Hop', 'Classical', 'Jazz'],
    'city': ['Delhi', 'Mumbai', 'Ahmedabad', 'Pune', 'Jaipur']
})

user_profiles = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'username': ['Rahul', 'Priya', 'Amit', 'Neha', 'Karan'],
    'city': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Jaipur']
})

result = pd.merge(playlists, user_profiles, on=['user_id', 'city'], how='inner')

print(result)
'''


# 5.Use ChatGPT or Copilot to generate sample code that merges two DataFrames: one for Flipkart products (product_id, name, category) and one for product ratings (rating_id, product_id, rating). Copy the code, run it, and modify it so that it performs a right join instead of the default.

'''
products = pd.DataFrame({
    'product_id': [101, 102, 103, 104],
    'name': ['Laptop', 'Smartphone', 'Headphones', 'Smartwatch'],
    'category': ['Electronics', 'Mobiles', 'Audio', 'Wearables']
})

ratings = pd.DataFrame({
    'rating_id': [1, 2, 3, 4, 5],
    'product_id': [101, 102, 105, 103, 102],
    'rating': [4.5, 4.2, 3.8, 4.0, 4.7]
})

result = pd.merge(products, ratings, on='product_id', how='right')

print(result)
'''