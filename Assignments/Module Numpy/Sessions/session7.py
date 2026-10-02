import numpy as np

# 1.Create two NumPy arrays representing the ratings of 5 restaurants on Zomato and Swiggy, then use np.concatenate() to combine them into a single array of 10 ratings and print the result.

zomato = np.array([3.8, 4.7, 4.1, 4.5, 4.9])
swiggy = np.array([4.8, 4.2, 4.7, 3.9, 4.3])

combined_array = np.concatenate((zomato, swiggy))
# print(combined_array) 

# 2.Given three arrays representing the number of likes on three different Instagram posts over 7 days, stack them vertically using np.vstack() so that each row represents one post's weekly likes, and print the stacked array.


post1 = np.array([120, 150, 180, 200, 220, 250, 300])
post2 = np.array([100, 140, 160, 190, 210, 230, 260])
post3 = np.array([130, 160, 170, 210, 240, 270, 310])

stackedarr = np.vstack((post1, post2, post3))
# print(stackedarr)

# 3.You have an array of 12 Flipkart product IDs. Use np.array_split() to divide this array into 5 nearly equal parts, and display each part.<br><br><em><strong>Hint:</strong> Check the shape of each split to confirm the division.</em>

prods = np.array(["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012"])

devidedarr = np.array_split(prods, 5)
# print(devidedarr)

# 4.Simulate a WhatsApp group chat: create a 2D NumPy array where each row is a user and each column is the number of messages sent per day for a week. Use np.insert() to add a new user (row) with their message counts, then use np.delete() to remove the user who sent the least messages overall.

messages = np.array([
    [12, 15, 10, 18, 20, 25, 22],  
    [ 8, 11, 14, 13, 17, 19, 21],  
    [20, 18, 22, 25, 24, 28, 30],  
    [ 5,  7,  9,  8, 10, 12, 11]   
])

updated_messages = np.insert(messages, 0, [11, 15, 17, 12, 8, 10, 14], axis=0)
# print(updated_messages)

total_msg = updated_messages.sum(axis=0)
# print(total_msg)

least_msg = np.argmin(total_msg, axis=0)
# print(least_msg)

new_msg = np.delete(updated_messages, 0, axis=0)
# print(new_msg)

# 5.Given a NumPy array of YouTube video view counts, use .view() to create a view and .copy() to create a copy. Modify the first element in each and print all arrays to demonstrate the difference between view and copy.<br><br><em><strong>Hint:</strong> Observe which changes affect the original array.</em>

temp_arr = np.array([1000, 2000, 3000, 4000])
print(f"ORIGINAL : {temp_arr}")

temp1 = temp_arr.view()
print(f"VIEW : {temp1}")
temp2 = temp_arr.copy()
print(f"COPY : {temp2}")

temp1[0] = 1111
print(f"View after update : {temp1}")
print(f"Original after view update : {temp_arr}")
# If changes done to view or origianl then it reflects in both array

temp2[0] = 999
print(f"COPY after update : {temp2}")
print(f"Original after copy update : {temp_arr}")
# If changes done to copy or origianl then it does not reflects in both array