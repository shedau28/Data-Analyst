# 1. head , tail  
# 2. info ,describe 
# 3. iloc ,loc 
# 4. query 
# 5. sort_values , sort_index, reset_index

import pandas as pd
import random
data = pd.read_csv("mckinsey.csv")
# print(data.head(7))
# print(data.tail(4))

# print(data[["country", "year", "population"]].head(10))

# print(data.describe().mean())

# print(data.loc[50:100,["country", "population", "life_exp"]])
# print(data.iloc[50:100,0:5:2])
"""
population > 100000000
AND
life_exp > 60"""

# print(data.query("population > 100000000 and life_exp > 60"))

# print(data.loc[(data["population"] > 100000000) & (data["life_exp"] > 60)])

# Find India's:

# population in 1952
# population in 2007
# life expectancy in 1952
# life expectancy in 2007
# GDP per capita in 1952
# GDP per capita in 2007


# res1 = data.query("country == 'India' and year == 1952")["population"]
# print(res1)
# res2 = data.query("country == 'India' and year == 2007")[["population", "life_exp", "gdp_cap"]]
# print(res2)
# res3 = data.query("country == 'India' and year == 1952")[["population", "life_exp", "gdp_cap"]]
# print(res3)

ranlist = random.sample(range(0,1704),1704)
# print(ranlist)
data.index = ranlist
# print(data.head(20))

# print(data.sort_index(ascending=True).head(20))

# data.reset_index(inplace=True)
# print(data.head(20))

data.sort_index(ascending=False)
print(data)
# data = data.reset_index(drop=True)
# print(data.head(20))
