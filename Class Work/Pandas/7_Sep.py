import pandas as pd

# data = pd.read_csv("customer_data (1).csv")
# print(data)

# select column from customer_data
# result = data['Name'] 
# print(result)


# select column from customer_data
# result = data[['Name', 'Age']]
# print(result)

#change column name
# data.rename(columns={"CustomerID" : "ID"}, inplace=True)

# print(data)


"""
HW
task  : 1 country  =="india" and year ==2002 print country  and year column using  loc or  iloc  or df . 
hint  : use & operator  for  condition 

a= df.loc[(df["country"]=="india") & (df["year"]==2002)]

task :2 in  mckinsey.csv dataset add new column col_name = next_year +3 display like  this  : 

    country,year,population,continent,life_exp,gdp_cap,next_year
0    Afghanistan,1952,8425333,Asia,28.801,779.4453145, 1955  
1    Afghanistan,1957,9240934,Asia,30.332,820.8530296, 1960
2    Afghanistan,1962,10267083,Asia,31.997,853.10071, 1965
3    Afghanistan,1967,11537966,Asia,34.02,836.1971382, 1970
4    Afghanistan,1972,13079460,Asia,36.088,739.9811058, 1975


"""
# task  : 1 country  =="india" and year ==2002 print country  and year column using  loc or  iloc  

data = pd.read_csv("mckinsey.csv")
# print(data.head())

# country = data.loc[(data['country']=='India') & (data['year']==2002)]
# print(country)


data['next_year'] = data['year'] + 3
print(data.head())