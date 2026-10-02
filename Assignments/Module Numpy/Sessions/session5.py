


import numpy as np

# 1.Create two NumPy arrays representing the number of likes on your last 7 Instagram posts and your friend's last 7 posts, then use np.add() and np.subtract() to calculate both the combined and difference arrays.

np.random.seed(100)
p1 = np.random.randint(100, 1000, 7)
np.random.seed(200)
p2 = np.random.randint(100, 1000, 7)

addarr = np.add(p1, p2)
subarr = np.subtract(p1, p2)

# print(addarr)
# print(subarr)



# 2.Given a NumPy array of item prices from your last Zomato order, use np.multiply() to apply a 10% discount on each item, then use np.sum() to calculate the final bill amount after discount.<br><br><em><strong>Hint:</strong> To apply a 10% discount, multiply each price by 0.9.</em>

price = np.random.randint(100, 1000, 5)
# print(price)

discounted_price = np.multiply(price, 0.9)
# print(discounted_price)

total_bill = np.sum(discounted_price)
# print(total_bill)


# 3.Take a NumPy array of daily step counts for the last 30 days (you can make up the numbers), and use np.mean(), np.median(), np.std(), and np.max() to analyze your fitness stats like a health app would.


steps = np.random.randint(1000, 10000, 30)
# print(steps)
# print(np.mean(steps))
# print(np.median(steps))
# print(np.std(steps))
# print(np.max(steps))


# 4.Create a NumPy array of 10 random float ratings (between 1 and 5) for a new movie on BookMyShow, then use np.round(), np.floor(), and np.ceil() to show how the rating would appear if rounded to the nearest whole number, always rounded down, and always rounded up.

rating = np.random.uniform(1, 5, 10)
# print(rating)
# print(np.round(rating))
# print(np.floor(rating))
# print(np.ceil(rating))


# 5.Use ChatGPT to generate Python code that calculates the percentage of songs you skipped in your last 20 Spotify plays using NumPy arrays and np.percentile(), then run the code and paste your output.<br><br><em><strong>Hint:</strong> Ask ChatGPT for code that finds the 75th percentile of skips in a NumPy array.</em>

# 1 = skipped, 0 = not skipped
plays = np.array([
    1, 0, 1, 0, 0,
    1, 0, 0, 1, 0,
    1, 0, 1, 0, 0,
    0, 1, 0, 1, 0
])

percentile = np.percentile(plays, 75)
print(percentile)












