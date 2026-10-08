import pandas as pd

# 1.Load the 'IPL_2023_Batsmen.csv' dataset (containing player name, runs, matches, average, strike rate) into a Pandas DataFrame and display the first 10 rows.

'''
ipl = pd.read_csv('IPL_2023_Batsmen.csv')

print(ipl.head(10))
'''

# 2.Perform univariate analysis on the 'runs' column: calculate and print the mean, median, mode, minimum, and maximum runs scored by batsmen in the IPL_2023_Batsmen dataset.

'''
print("Mean:", ipl['runs'].mean())
print("Median:", ipl['runs'].median())
print("Mode:", ipl['runs'].mode()[0])
print("Minimum:", ipl['runs'].min())
print("Maximum:", ipl['runs'].max())

'''

# 3.Create a Pandas DataFrame for your top 5 favorite Zomato restaurants with columns: 'name', 'rating', 'votes', and 'avg_cost'. Perform bivariate analysis between 'rating' and 'votes' by calculating their correlation coefficient.
'''
zomato = pd.DataFrame({
    'name': ['Restaurant A', 'Restaurant B', 'Restaurant C', 'Restaurant D', 'Restaurant E'],
    'rating': [4.5, 4.2, 4.7, 4.0, 4.4],
    'votes': [1200, 850, 1500, 600, 1100],
    'avg_cost': [800, 600, 1000, 500, 750]
})

correlation = zomato['rating'].corr(zomato['votes'])

print("Correlation coefficient:", correlation)
'''
# 4.Generate summary statistics (count, mean, std, min, 25%, 50%, 75%, max) for all numeric columns in the IPL_2023_Batsmen DataFrame using the describe() function and interpret any one interesting insight you observe.<br><br><em><strong>Hint:</strong> Look for outliers or surprising averages in the summary.</em>
'''
print(ipl.describe())
'''

# 5.Use ChatGPT to suggest two additional univariate or bivariate analyses you could perform on the IPL_2023_Batsmen dataset, then implement one of them in code and show the output.

'''
correlation = ipl['runs'].corr(ipl['strike rate'])

print(correlation)
'''