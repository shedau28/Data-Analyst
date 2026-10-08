import pandas as pd

# 1.Download a CSV file of IPL cricket players with columns for player name, team, and age, then use pandas to load it and print out all rows where the age column has missing values.
'''
data = pd.read_csv('imp_players.csv')
print(data.isna())
print(data[data['age'].isna()])
'''


# 2.Using a dataset of food delivery orders (with columns: order_id, customer_name, delivery_rating), use pandas to drop all rows where the delivery_rating is missing and display the cleaned DataFrame.
'''
data = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_name': ['Rahul', 'Priya', 'Amit', 'Neha', 'Karan'],
    'delivery_rating': [4.5, None, 4.0, None, 5.0]
})
print(data)
new_data = data.dropna(subset=['delivery_rating'])
print(new_data)
'''

# 3.Given a Flipkart-style product reviews dataset with some missing 'rating' values, use pandas to fill all missing ratings with the mean rating of the dataset and print the updated DataFrame.<br><br><em><strong>Hint:</strong> Use the fillna() method with the mean() function.</em>
'''
data = pd.DataFrame({
    'product_name': ['iPhone 15', 'Samsung Galaxy M14', 'HP Laptop', 'boAt Headphones', 'Nike Shoes', 'Redmi Note 13'],
    'rating': [4.5, 4.2, None, 4.0, 4.3, None]
})
mean_data = data['rating'].mean()
new_data = data.fillna(value=mean_data)
print(new_data)
'''

# 4.You have a Spotify playlist CSV with missing 'duration' values for some songs. Replace all missing durations with the median duration of the available songs using pandas, then save the cleaned DataFrame to a new CSV file.
'''
data = pd.read_csv('spotify_playlist.csv')
print(data)
new_Data = data.fillna(value=data['duration'].median())
print(new_Data)
new_Data.to_csv("cleaned_sportyfy.csv")
'''

# 5.Use ChatGPT to generate pandas code that replaces all missing values in a 'followers' column (from a simulated Instagram user data CSV) with 0, then test the code on your own sample data and submit both the code and the result.<br><br><em><strong>Hint:</strong> Ask ChatGPT: 'How do I replace missing values in a pandas DataFrame column with zero?'</em>
'''
data = pd.DataFrame({
    'username': ['user1', 'user2', 'user3', 'user4', 'user5'],
    'followers': [1200, None, 3500, None, 800]
})
print(data)

new_data = data.fillna(value=0)
print(new_data)
'''