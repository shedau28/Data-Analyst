
import pandas as pd

# 1.Install pandas in your Python environment and create a Series named 'fav_cricket_teams' containing the names of your 5 favorite IPL teams. Print the Series.
'''
data = pd.Series(['GT', 'RCB', 'MI', 'SRH'])
print(data)
'''

# 2.Create a DataFrame named 'food_orders' with columns: 'Item', 'Restaurant', and 'Price'. Add 3 rows representing your last 3 Zomato or Swiggy orders and display the DataFrame.
'''
data = pd.DataFrame({
    'Item' : [3,1,2],
    'Restaurant' : ['Rest1', 'Rest2', 'Rest3'],
    'Price' : [1000, 2000, 3000]
})
print(data)
'''

# 3.Given a list of follower counts for 5 Instagram influencers: [1200, 54000, 780, 150000, 32000], create a pandas Series called 'followers', then print the influencer(s) with the highest and lowest follower counts.<br><br><em><strong>Hint:</strong> Use Series.idxmax() and Series.idxmin() to find the indices.</em>
'''
followers = pd.Series([1200, 54000, 780, 150000, 32000])
print(followers.idxmin())
print(followers.idxmax())
'''

# 4.Create a DataFrame called 'playlist' with columns: 'Song', 'Artist', and 'Duration' (in minutes). Enter details for 4 songs you recently listened to on Spotify or YouTube Music, then print only the 'Song' and 'Duration' columns.
'''
playlist = pd.DataFrame({
    'Song': ['Blinding Lights', 'Shape of You', 'Perfect', 'Believer'],
    'Artist': ['The Weeknd', 'Ed Sheeran', 'Ed Sheeran', 'Imagine Dragons'],
    'Duration': [3.20, 4.24, 4.23, 3.24]
})
print(playlist[['Song','Duration']])
'''


