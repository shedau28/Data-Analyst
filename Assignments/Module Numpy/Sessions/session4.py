


import numpy as np

# 1.Create two NumPy arrays: one representing the number of likes on your last 7 Instagram posts, and another for the number of comments. Use arithmetic operators to calculate the average engagement (likes + comments) per post and print the result.

likes = np.random.randint(100, 1000, 7)
cmnts = np.random.randint(1000, 10000, 7)

# print(f"LIKES : {likes} \nCOMMENTS : {cmnts}")

result = likes + cmnts
# print(result)

# 2.Given two NumPy arrays: one with the prices of 5 food items on Zomato and another with the corresponding discounts in rupees, use element-wise subtraction to get the final price for each item and display the array.

price = np.random.randint(100, 1000, 5)
discount = np.random.randint(10, 50, 5)
# print(price)
# print(discount)
final_price = np.subtract(price, discount)
# print(final_price)



# 3.Suppose you have a NumPy array of IPL team scores for 5 matches. Use comparison operators to create a boolean array indicating which matches had scores greater than 180, then print the boolean array.<br><br><em><strong>Hint:</strong> Use the '>' operator directly on the array.</em>


score = np.random.randint(100, 250, 5)
# print(score)
result2 = score > 180
# print(result2)


# 4.Create two NumPy arrays: one showing whether a user paid via Paytm (1 for paid, 0 for not) and another for PhonePe for 6 transactions. Use np.logical_or() to find out which transactions were paid by either app and print the result.

paytm = np.array([1, 0, 0, 0, 1, 0])
phonepay = np.array([0, 1, 0, 1, 0, 1])

final = np.logical_or(paytm, phonepay)
# print(final)


# 5.Given a NumPy array of the number of steps you walked each day for a week, use broadcasting to add a bonus of 500 steps to each day's count, then calculate and print the total steps for the week using an aggregate operation.

steps = np.random.randint(1000, 10000, 7)
# print(steps)

new_steps = steps + 500
# print(new_steps)

total = np.sum(new_steps)
# print(total)













