import pandas as pd

# 1.Download a publicly available CSV dataset of IPL cricket matches (for example, from Kaggle or data.world), and use pandas to load it into a DataFrame named ipl_df. Display the first 5 rows.
'''
ipl_df = pd.read_csv('IPL_Matches_2008_2023.csv')

print(ipl_df.head(5))
'''
# 2.Clean the ipl_df DataFrame by removing any rows where the 'winner' column is missing or null, and reset the index afterwards.
'''
ipl_df = ipl_df.dropna(subset=['winner']).reset_index(drop=True)

print(ipl_df.head())
'''
# 3.Transform the ipl_df DataFrame to add a new column 'match_margin_type' that labels each match as 'Runs' if the 'win_by_runs' value is greater than 0, 'Wickets' if 'win_by_wickets' is greater than 0, or 'Tie/No Result' otherwise.<br><br><em><strong>Hint:</strong> Use numpy.select() or pandas' apply() for this transformation.</em>

'''
conditions = [
    ipl_df['win_by_runs'] > 0,
    ipl_df['win_by_wickets'] > 0
]

choices = ['Runs', 'Wickets']

ipl_df['match_margin_type'] = np.select(
    conditions,
    choices,
    default='Tie/No Result'
)

print(ipl_df[['team1', 'team2', 'winner', 'match_margin_type']].head())
'''

# 4.Merge the ipl_df DataFrame with a separate DataFrame containing IPL team names and their home cities (create this manually with at least 5 teams), using the team name as the key, and add the home city for both 'team1' and 'team2' in each match.
'''
teams = pd.DataFrame({
    'team': ['Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore',
             'Kolkata Knight Riders', 'Rajasthan Royals', 'Delhi Capitals'],
    'home_city': ['Mumbai', 'Chennai', 'Bengaluru', 'Kolkata', 'Jaipur', 'Delhi']
})

team_city = teams.set_index('team')['home_city']

ipl_df['team1_home_city'] = ipl_df['team1'].map(team_city)
ipl_df['team2_home_city'] = ipl_df['team2'].map(team_city)

print(ipl_df[['team1', 'team1_home_city', 'team2', 'team2_home_city']].head())
'''

# 5.Create a pivot table to show the total number of matches won by each team per season, and display the top 3 teams with the most wins in any single season.
'''
wins = ipl_df.groupby(['season', 'winner']).size().reset_index(name='wins')

pivot = wins.pivot_table(
    index='season',
    columns='winner',
    values='wins',
    fill_value=0
)

top_3 = wins.sort_values('wins', ascending=False).head(3)

print(pivot)
print(top_3)
'''