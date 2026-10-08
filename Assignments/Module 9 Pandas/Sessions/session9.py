import pandas as pd

# 1.Create a Pandas Series of 5 random date strings in the format 'DD-MM-YYYY', then convert this Series to datetime objects using pd.to_datetime and print the result.
'''
dates = pd.Series([
    '15-03-2024',
    '27-07-2023',
    '05-01-2025',
    '19-11-2022',
    '30-09-2024'
])

dates = pd.to_datetime(dates, format='%d-%m-%Y')

print(dates)
'''

# 2.Given a DataFrame with a 'release_date' column containing movie release dates (as strings), add three new columns: 'year', 'month', and 'day' by extracting these values from the 'release_date' column using Pandas.<br><br><em><strong>Hint:</strong> Use the .dt accessor after converting to datetime.</em>

'''
movies = pd.DataFrame({
    'title': ['3 Idiots', 'Dangal', 'Jawan', 'Pathaan'],
    'release_date': ['25-12-2009', '23-12-2016', '07-09-2023', '25-01-2023']
})

movies['release_date'] = pd.to_datetime(movies['release_date'], format='%d-%m-%Y')

movies['year'] = movies['release_date'].dt.year
movies['month'] = movies['release_date'].dt.month
movies['day'] = movies['release_date'].dt.day

print(movies)
'''


# 3.Generate a date range for the next 7 days starting from today using pd.date_range, and display the list of dates in the console.

'''
dates = pd.date_range(start=pd.Timestamp.today().normalize(), periods=7)

print(dates)
'''

# 4.Suppose you have a DataFrame of Zomato Gold subscriptions with columns 'user_id' and 'start_date' (as strings). Calculate the tenure (in days) for each user by subtracting the 'start_date' from today's date, and add it as a new column 'tenure_days'.<br><br><em><strong>Hint:</strong> Use pd.to_datetime for conversion and (today - start_date).dt.days for calculation.</em>


'''
data = pd.DataFrame({
    'user_id': [101, 102, 103, 104, 105],
    'start_date': ['01-01-2025', '15-06-2025', '20-09-2024', '10-02-2026', '25-05-2025']
})

data['start_date'] = pd.to_datetime(data['start_date'], format='%d-%m-%Y')

today = pd.Timestamp.today().normalize()
data['tenure_days'] = (today - data['start_date']).dt.days

print(data)
'''