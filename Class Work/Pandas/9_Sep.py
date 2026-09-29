import pandas as pd

# country = Egypy, life > 50

data = pd.read_csv("mckinsey.csv")
print(data.head(20))

# result = data.loc[(data['country']=="Egypt") & (data["life_exp"] > 50)]
# result = data.query("country == 'Egypt' and life_exp > 50")
# print(result)

# result2 = data.loc[data["gdp_cap"] > 800]
# print(result2["country"])

# data.sort_values(by="population",ascending=False, inplace=True)

data.sort_index(ascending=True, inplace=True)

print(data.head(20))
# hw  : 
"""
1. head , tail  
2. info ,describe 
3. iloc ,loc 
4. query 
5. sort_values , sort_index, reset_index
"""

