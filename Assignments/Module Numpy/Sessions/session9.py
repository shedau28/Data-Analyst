import numpy as np

# 1.Create a NumPy array named prices with these values: [299, 499, 799, 0, 1599, -1, 899]. Print the array and its data type.

prices = np.array([299, 499, 799, 0, 1599, -1, 899])
print(prices)
print(prices.dtype)


# 2.Some entries in the prices array are invalid (0 or negative). Replace all values less than or equal to zero with the average of the remaining positive prices.<br><br><em><strong>Hint:</strong> Use boolean indexing and the mean() function.</em>



# 3.Suppose you have a NumPy array quantities = [2, 1, 3, 4, 2, 1, 5]. Calculate the total bill for each item by multiplying the cleaned prices array with quantities, and print the resulting array.
# 4.Generate and print a summary report: show the minimum, maximum, average, and total of the cleaned prices array, and also the total bill for all items combined.<br><br><em><strong>Hint:</strong> Use NumPy functions like min(), max(), mean(), and sum().</em>
# 5.Use ChatGPT or Copilot to suggest a NumPy function or method that can help you find out how many unique price values are present in your cleaned prices array. Try the suggested method and print the result.