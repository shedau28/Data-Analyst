
import pandas as pd

# 1) Create a series of three different colors 
'''
data = pd.Series(["Red", "Blue", "Green"])
'''

# 2) View the series of different colors 
'''
print(data)
'''

# 3) Create a series of three different car types and view it
'''
cars = pd.Series(["Toyota", "BMW", "Audi", "Honda"])
print(cars)
'''

# 4) Combine the Series of cars and colors into a Data Frame
'''
data = pd.DataFrame({
    'Colors' : ["Red", "Blue", "Green", "Yellow"],
    'Cars' : ["Toyota", "BMW", "Audi", "Honda"]
})

print(data)
'''

# 5) Find the different datatypes of the car data Data Frame 
'''
cars = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda"],
    "Price": [1500000, 5000000, 4500000, 1200000],
    "Year": [2020, 2022, 2021, 2019],
    "Electric": [False, True, True, False]
})
print(cars.dtypes)
'''

# 6) Describe your current car sales Data Frame using describe ()
'''
cars = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda"],
    "Price": [1500000, 5000000, 4500000, 1200000],
    "Year": [2020, 2022, 2021, 2019],
    "Electric": [False, True, True, False]
})
print(cars.describe)
'''

# 7) Get information about your Data Frame using info () 
'''
cars = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda"],
    "Price": [1500000, 5000000, 4500000, 1200000],
    "Year": [2020, 2022, 2021, 2019],
    "Electric": [False, True, True, False]
})
print(cars.info())
'''

# 8) Create a Series of different numbers and find the mean of them 
'''
data = pd.Series([1,2,3,4,5,6])
print(data.mean())
'''

# 9) Create a Series of different numbers and find the sum of them 
'''
data = pd.Series([1,2,3,4,5,6])
print(data.sum())
'''

# 10) List out all the column names of the car sales Data Frame 
'''
cars = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda"],
    "Price": [1500000, 5000000, 4500000, 1200000],
    "Year": [2020, 2022, 2021, 2019],
    "Electric": [False, True, True, False]
})
print(cars.columns)
'''

# 11) Find the length of the car sales Data Frame 
'''
cars = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda"],
    "Price": [1500000, 5000000, 4500000, 1200000],
    "Year": [2020, 2022, 2021, 2019],
    "Electric": [False, True, True, False]
})
print(len(cars))
'''

# 12) Show the first 3 rows of the car sales Data Frame 
'''
car_sales = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda", "Hyundai",
              "Tata", "Ford", "Kia", "Mercedes", "Mahindra"],

    "Model": ["Fortuner", "X5", "A4", "City", "Creta",
              "Nexon", "Endeavour", "Seltos", "C-Class", "XUV700"],

    "Year": [2022, 2023, 2021, 2020, 2023,
             2022, 2021, 2023, 2022, 2024],

    "Price": [4200000, 8500000, 4800000, 1500000, 1800000,
              1400000, 3500000, 1700000, 6500000, 2600000],

    "Quantity": [5, 2, 3, 8, 10,
                 12, 4, 9, 2, 7],

    "Fuel_Type": ["Diesel", "Petrol", "Petrol", "Petrol", "Diesel",
                  "Petrol", "Diesel", "Petrol", "Petrol", "Diesel"]
})
print(car_sales.head())
'''

# 13) Show the first 7 rows of the car sales Data Frame
'''
car_sales = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda", "Hyundai",
              "Tata", "Ford", "Kia", "Mercedes", "Mahindra"],

    "Model": ["Fortuner", "X5", "A4", "City", "Creta",
              "Nexon", "Endeavour", "Seltos", "C-Class", "XUV700"],

    "Year": [2022, 2023, 2021, 2020, 2023,
             2022, 2021, 2023, 2022, 2024],

    "Price": [4200000, 8500000, 4800000, 1500000, 1800000,
              1400000, 3500000, 1700000, 6500000, 2600000],

    "Quantity": [5, 2, 3, 8, 10,
                 12, 4, 9, 2, 7],

    "Fuel_Type": ["Diesel", "Petrol", "Petrol", "Petrol", "Diesel",
                  "Petrol", "Diesel", "Petrol", "Petrol", "Diesel"]
})
# print(car_sales.head(7))
'''

# 14) Show the bottom 5 rows of the car sales Data Frame 
'''
print(car_sales.tail(7))
'''

# 15) Use. loc to select the row at index 3 of the car sales Data Frame
'''
car_sales = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda", "Hyundai",
              "Tata", "Ford", "Kia", "Mercedes", "Mahindra"],

    "Model": ["Fortuner", "X5", "A4", "City", "Creta",
              "Nexon", "Endeavour", "Seltos", "C-Class", "XUV700"],

    "Year": [2022, 2023, 2021, 2020, 2023,
             2022, 2021, 2023, 2022, 2024],

    "Price": [4200000, 8500000, 4800000, 1500000, 1800000,
              1400000, 3500000, 1700000, 6500000, 2600000],

    "Quantity": [5, 2, 3, 8, 10,
                 12, 4, 9, 2, 7],

    "Fuel_Type": ["Diesel", "Petrol", "Petrol", "Petrol", "Diesel",
                  "Petrol", "Diesel", "Petrol", "Petrol", "Diesel"]
})
print(car_sales.loc[3])
'''

# 16) Use. iloc to select the row at position 3 of the car sales Data Frame 
'''
car_sales = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda", "Hyundai",
              "Tata", "Ford", "Kia", "Mercedes", "Mahindra"],

    "Model": ["Fortuner", "X5", "A4", "City", "Creta",
              "Nexon", "Endeavour", "Seltos", "C-Class", "XUV700"],

    "Year": [2022, 2023, 2021, 2020, 2023,
             2022, 2021, 2023, 2022, 2024],

    "Price": [4200000, 8500000, 4800000, 1500000, 1800000,
              1400000, 3500000, 1700000, 6500000, 2600000],

    "Quantity": [5, 2, 3, 8, 10,
                 12, 4, 9, 2, 7],

    "Fuel_Type": ["Diesel", "Petrol", "Petrol", "Petrol", "Diesel",
                  "Petrol", "Diesel", "Petrol", "Petrol", "Diesel"]
})
print(car_sales.iloc[2])
'''

# 17) Create a crosstab of the Make and Doors columns. 
'''
car_sales = pd.DataFrame({
    "Brand": ["Toyota", "BMW", "Audi", "Honda", "Hyundai",
              "Tata", "Ford", "Kia", "Mercedes", "Mahindra"],

    "Model": ["Fortuner", "X5", "A4", "City", "Creta",
              "Nexon", "Endeavour", "Seltos", "C-Class", "XUV700"],

    "Year": [2022, 2023, 2021, 2020, 2023,
             2022, 2021, 2023, 2022, 2024],

    "Price": [4200000, 8500000, 4800000, 1500000, 1800000,
              1400000, 3500000, 1700000, 6500000, 2600000],

    "Quantity": [5, 2, 3, 8, 10,
                 12, 4, 9, 2, 7],

    "Fuel_Type": ["Diesel", "Petrol", "Petrol", "Petrol", "Diesel",
                  "Petrol", "Diesel", "Petrol", "Petrol", "Diesel"]
})

print(pd.crosstab(car_sales['Brand'], car_sales['Year']))
'''


