import pandas as pd


# 1.Create a DataFrame named 'movies' with columns: 'title', 'rating', and 'release_year' for at least 6 popular Bollywood films. Use sort_values() to display the movies sorted by 'rating' from highest to lowest.

'''
movies = pd.DataFrame({
    'title': ['3 Idiots', 'Dangal', 'Lagaan', 'Zindagi Na Milegi Dobara', 'Taare Zameen Par', 'Andhadhun'],
    'rating': [8.4, 8.3, 8.1, 8.2, 8.3, 8.2],
    'release_year': [2009, 2016, 2001, 2011, 2007, 2018]
})
print(movies.sort_values(by='rating', ascending=False))
'''


# 2.Given a DataFrame of IPL teams with columns 'team', 'points', and 'net_run_rate', use sort_index() to sort the DataFrame by the default index in descending order, then print the result.<br><br><em><strong>Hint:</strong> Use the ascending parameter in sort_index().</em>
'''
ipl = pd.DataFrame({
    'team': ['MI', 'CSK', 'RCB', 'KKR', 'RR', 'SRH'],
    'points': [16, 14, 18, 12, 14, 10],
    'net_run_rate': [0.45, 0.32, 0.75, 0.21, 0.36, -0.12]
})

print(ipl.sort_index(ascending=False))
'''

# 3.Reset the index of a DataFrame containing a list of trending YouTube videos (columns: 'video_title', 'views', 'likes'), and make sure the old index is not added as a column in the result.<br><br><em><strong>Constraint:</strong> Use the drop=True argument in reset_index().</em>
'''
youtube = pd.DataFrame({
    'video_title': ['Music Video', 'Funny Moments', 'Cricket Highlights', 'Tech Review', 'Travel Vlog'],
    'views': [5000000, 3200000, 4500000, 1800000, 2100000],
    'likes': [450000, 280000, 390000, 150000, 190000]
}, index=[5, 2, 8, 1, 6])
print(youtube)
new_yt = youtube.reset_index(drop=True)
print(new_yt)
'''

# 4.You have a DataFrame of Zomato restaurant names and their ratings. Use reindex() to rearrange the rows so that your favorite restaurant appears first, followed by the rest in any order.
'''
zomato = pd.DataFrame({
    'restaurant': ['Dominos', 'Haldirams', 'McDonalds', 'Pizza Hut', 'Subway'],
    'rating': [4.2, 4.5, 4.1, 4.0, 4.3]
}, index=['A', 'B', 'C', 'D', 'E'])

print(zomato)
zomato = zomato.reindex(['C', 'A', 'B', 'D', 'E'])
print(zomato)
'''


# 5.Take a DataFrame of Flipkart products with columns 'product_name', 'price', and 'discount'. First, sort the products by 'discount' descending, then reset the index so it starts from 0 and is sequential after sorting.
'''
flipkart = pd.DataFrame({
    'product_name': ['iPhone 15', 'Samsung Galaxy M14', 'HP Laptop', 'boAt Headphones', 'Nike Shoes'],
    'price': [69999, 11490, 38990, 1499, 2499],
    'discount': [10, 25, 15, 40, 30]
})
print(flipkart)
data = flipkart.sort_values(by='discount', ascending=False)

data = data.reset_index(drop=True)
print(data)
'''