

import numpy as np

# 1.Create a NumPy array called prices with the following values: [199, 299, 399, 499, 599]. Use basic indexing to print the first and last price.

prices = np.array([199, 299, 399, 499, 599])
# print(f"First - {prices[0]} And Last - {prices[-1]}")


# 2.Given a 2D NumPy array representing cricket scores for 3 players across 5 matches, use slicing to extract the scores of all players for matches 2 to 4 (index 1 to 3).

scores = np.array([
    [45, 67, 23, 89, 56],   
    [78, 34, 56, 45, 90],   
    [32, 88, 41, 67, 55]    
])
# print(scores[:,1:4])


# 3.You have a NumPy array called ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5]). Use negative indexing to print the last three ratings.

ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5])
# print(ratings[-1 : -4: -1])


# 4.Create a NumPy array of the first 20 natural numbers. Use step slicing to print every 3rd number starting from the second element.<br><br><em><strong>Hint:</strong> Use the slice notation with a step value.</em>

natural_numbers = np.arange(1, 21)
# print(natural_numbers[1::3])


# 5.Given a NumPy array of Flipkart product prices, use boolean indexing to extract all prices greater than 500. Print the resulting array.


flip_prices = np.array([200, 599, 699, 499, 444])
bool_price = flip_prices > 500
# print(bool_price)


# 6.You have an array of IPL team scores: np.array([210, 180, 195, 220, 205, 175]). Use np.where() to find the indices of all scores above 200 and print these indices.

scores = np.array([210, 180, 195, 220, 205, 175])
print(np.where(scores > 200))


