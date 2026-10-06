import numpy as np


# 1.Given a NumPy array of IPL team names with some duplicates, use np.unique() to print a sorted list of all unique team names.

teams = np.array(["CSK","MI","RCB","KKR","SRH","DC","PBKS","RR","GT","LSG","MI","CSK","RCB","MI","KKR","RR","CSK","GT"])

unique_teams = np.unique(teams)
# print(unique_teams)

# 2.Create a NumPy array of Zomato order ratings (with some NaN values), then use np.isnan() to count how many ratings are missing.

ratings = np.array([4.5,3.0,np.nan,5.0,2.5,np.nan,4.0,3.5,np.nan,4.5,1.5,5.0])

# print(np.isnan(ratings).sum())


# 3.Given an array of Flipkart product prices, use np.clip() to limit all prices between 100 and 1000, and print the resulting array.<br><br><em><strong>Hint:</strong> Use np.clip(array, 100, 1000).</em>

prices = np.array([499, 1299, 2499, 799, 1599, 3499, 999, 5999, 1899, 2999, 749, 4299])
prices = np.clip(prices, 100, 1000)
# print(prices)

# 4.You have a NumPy array of YouTube video view counts, some of which are NaN or inf. Replace all NaN values with 0, and all inf values with the maximum finite value in the array.

views = np.array([1250, 4500, np.nan, 8900, np.inf, 3200, 7500, np.nan, 15000, np.inf, 5600])
views[np.isnan(views)] = 0
print(views)
np.


# 5.Use ChatGPT to generate a Python code snippet that finds the indices of all even numbers in a NumPy array using np.where(), then test the code with your own example array.


