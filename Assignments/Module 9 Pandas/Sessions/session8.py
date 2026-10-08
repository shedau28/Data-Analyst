import pandas as pd


# 1.Create a Pandas DataFrame with a column 'username' containing 5 Instagram usernames in mixed case (e.g., 'CoolDude', 'foodieQueen', etc.), then use str.lower to convert all usernames to lowercase and print the result.
'''
df = pd.DataFrame({
    'username': ['CoolDude', 'foodieQueen', 'TechGuru', 'TravelLover', 'InstaStar']
})

df['username'] = df['username'].str.lower()

print(df)
'''
# 2.Given a Pandas Series of song titles from your Spotify playlist, use str.replace to remove all occurrences of the word 'Remix' from the titles and display the cleaned list.

'''
songs = pd.Series([
    'Blinding Lights Remix',
    'Shape of You',
    'Perfect Remix',
    'Levitating Remix',
    'Believer'
])

songs = songs.str.replace('Remix', '', regex=False).str.strip()

print(songs)
'''

# 3.You have a DataFrame with a 'review' column containing user reviews from Zomato. Use str.contains to filter and display only the reviews that mention the word 'delivery'.<br><br><em><strong>Hint:</strong> Remember to handle case sensitivity so that 'Delivery' and 'delivery' are both matched.</em>
'''
df = pd.DataFrame({
    'review': [
        'Fast delivery and good food',
        'The food was delicious',
        'Delivery was very late',
        'Excellent restaurant',
        'Quick Delivery service'
    ]
})

result = df[df['review'].str.contains('delivery', case=False, na=False)]
'''


# 4.Take a Pandas Series of Flipkart product categories in the format 'Electronics/Mobiles/Smartphones', 'Home/Kitchen/Appliances', etc. Use str.split to extract just the main category (the part before the first '/') and create a new column with these values.

'''
df = pd.DataFrame({
    'category': [
        'Electronics/Mobiles/Smartphones',
        'Home/Kitchen/Appliances',
        'Fashion/Men/Shirts',
        'Beauty/Makeup/Lipstick',
        'Sports/Cricket/Bats'
    ]
})

df['main_category'] = df['category'].str.split('/').str[0]

print(df)
'''

# 5.Given a DataFrame of YouTube video titles, use str.upper to convert all titles to uppercase, then chain str.replace to substitute every space with an underscore.<br><br><em><strong>Constraint:</strong> Do this in a single line of code for the transformation.</em>

'''
df = pd.DataFrame({
    'title': [
        'Best Cricket Highlights',
        'Python Tutorial For Beginners',
        'Top Bollywood Songs',
        'Amazing Travel Vlog',
        'How To Cook Pasta'
    ]
})

df['title'] = df['title'].str.upper().str.replace(' ', '_', regex=False)

print(df)
'''