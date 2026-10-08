import pandas as pd
import numpy as np
from scipy.stats import zscore

# 1.Load a CSV file of Spotify song streams (with columns: song, artist, streams, date) into a pandas DataFrame and use drop_duplicates() to remove any duplicate song entries, keeping only the first occurrence.
'''
data = pd.read_csv('spotify_streams.csv')
print(data)
data.drop_duplicates(subset=['song'])
print(data)
'''

# 2.Given a pandas DataFrame of Flipkart product reviews with columns: product_id, user_id, rating, review_text, identify and print the number of duplicate reviews (where product_id and user_id are both the same) before and after using drop_duplicates().
'''
data = pd.DataFrame({
    'product_id': [101, 102, 101, 103, 102, 104, 101],
    'user_id': [1, 2, 1, 3, 2, 4, 5],
    'rating': [5, 4, 5, 3, 4, 5, 4],
    'review_text': ['Excellent', 'Good', 'Excellent', 'Average', 'Good', 'Excellent', 'Nice']
})
# print(data)
print(data.duplicated(subset=['product_id', 'user_id']).sum())
new_data = data.drop_duplicates(subset=['product_id', 'user_id'])
print(new_data)
'''


# 3.Use the IQR method to detect outliers in the 'order_amount' column of a Zomato orders DataFrame and print the order IDs that are considered outliers.<br><br><em><strong>Hint:</strong> Calculate Q1, Q3, and IQR, then filter orders outside the [Q1 - 1.5*IQR, Q3 + 1.5*IQR] range.</em>
'''
data = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'order_amount': [250, 450, 500, 550, 600, 650, 700, 2000]
})

print(data)
q1 = np.quantile(data['order_amount'], 0.25)
q3 = np.quantile(data['order_amount'], 0.75)
print(q1, q3)

iqr = q3-q1
print('IQR ', iqr)

lower_bound = q1 - iqr*1.5
upper_bound = q3 + iqr*1.5

print(lower_bound)
print(upper_bound)

outliers = data[(data['order_amount']<lower_bound) | (data['order_amount']>upper_bound)]['order_id']
print(outliers)
'''

# 4.For a DataFrame containing daily IPL match ticket sales (columns: date, tickets_sold), calculate the Z-score for each day's tickets_sold, and print the dates where the absolute Z-score is greater than 2.<br><br><em><strong>Constraint:</strong> Use pandas and scipy.stats.zscore for calculations.</em>
'''
data = pd.DataFrame({
    'date': ['2026-04-01', '2026-04-02', '2026-04-03', '2026-04-04', '2026-04-05',
             '2026-04-06', '2026-04-07', '2026-04-08'],
    'tickets_sold': [12000, 13500, 12800, 14000, 13200, 12500, 13000, 30000]
})
data['z_score'] = zscore(data['tickets_sold'])
outliers = data[abs(data['z_score']) > 2]
print(outliers['date'])
'''

# 5.Use ChatGPT or Copilot to generate a pandas function that finds and returns all outlier transaction amounts in a Paytm wallet DataFrame using the Z-score method, then test the function with sample data.
'''
data = pd.DataFrame({
    'transaction_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'transaction_amount': [250, 300, 450, 200, 350, 400, 275, 5000]
})

def find_outliers(data):
    z_scores = zscore(data['transaction_amount'])
    return data[abs(z_scores) > 2]


outliers = find_outliers(data)

print(outliers)
'''

