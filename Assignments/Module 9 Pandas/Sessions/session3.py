import pandas as pd

# 1.Download a CSV file containing a list of movies with columns like 'title', 'genre', 'rating', and 'box_office', then use pandas to load this file and select only the 'title' and 'rating' columns using the loc method.
'''
data = pd.read_csv('movies.csv')
print(data.loc[:,['title', 'rating']])
'''

# 2.Given a DataFrame of Flipkart products with columns 'product_name', 'category', and 'price', use iloc to select the first 10 rows and all columns, and print the result.
'''
df = pd.DataFrame({'product_name':['Samsung Galaxy M14','iPhone 15','Redmi Note 13','OnePlus Nord CE 3','boAt Rockerz 450','Sony WH-1000XM5','HP 15s Laptop','Dell Inspiron 15','Lenovo IdeaPad Slim 3','Nike Running Shoes','Adidas Sneakers','Puma Sports Shoes','Levis Men T-Shirt','Allen Solly Shirt','Pigeon Induction Cooktop','Prestige Mixer Grinder','Philips Air Fryer','Canon Printer','Mi Smart TV 43','Realme Smartwatch'],'category':['Mobiles','Mobiles','Mobiles','Mobiles','Audio','Audio','Laptops','Laptops','Laptops','Footwear','Footwear','Footwear','Clothing','Clothing','Kitchen Appliances','Kitchen Appliances','Kitchen Appliances','Printers','Televisions','Wearables'],'price':[11490,69999,13999,24999,1499,29999,38990,45990,36990,2499,2999,2199,999,1499,1449,3299,5999,8499,24999,3999]})

print(df.iloc[0:10])
'''


# 3.Using a DataFrame of food orders from Zomato with columns 'restaurant', 'order_amount', and 'delivery_time', filter and display only those orders where 'order_amount' is greater than 500 using a boolean condition.
'''
data = pd.DataFrame({
    'restaurant': ['Dominos', 'McDonalds', 'Pizza Hut', 'Biryani Blues', 'KFC', 'Subway', 'Burger King', 'Haldirams'],
    'order_amount': [650, 450, 750, 900, 550, 350, 620, 800],
    'delivery_time': [35, 25, 40, 45, 30, 20, 35, 50]
})

print(data[data['order_amount'] > 500])
'''

# 4.Given a DataFrame of Spotify songs with columns 'song', 'artist', 'streams', and 'duration', use the query() method to select all songs with more than 1,000,000 streams and duration less than 180 seconds.<br><br><em><strong>Hint:</strong> Use the query syntax: query('streams > 1000000 and duration < 180')</em>
'''
data = pd.DataFrame({
    'song': ['Blinding Lights', 'Shape of You', 'Perfect', 'Levitating', 'Believer', 'Stay', 'Heat Waves', 'As It Was'],
    'artist': ['The Weeknd', 'Ed Sheeran', 'Ed Sheeran', 'Dua Lipa', 'Imagine Dragons', 'The Kid LAROI', 'Glass Animals', 'Harry Styles'],
    'streams': [4000000, 3500000, 2500000, 1800000, 1200000, 900000, 2200000, 1500000],
    'duration': [200, 150, 263, 203, 204, 141, 138, 167]
})
data = data.query('streams > 1000000 & duration < 180')
print(data)
'''

# 5.Suppose you have a DataFrame of IPL cricket matches with columns 'team1', 'team2', 'winner', and 'total_runs'. Write code to filter and display all matches where 'total_runs' is between 180 and 220 using boolean indexing.<br><br><em><strong>Constraint:</strong> Do not use the query() method for this task.</em>
'''
data = pd.DataFrame({
    'team1': ['MI', 'CSK', 'RCB', 'KKR', 'RR', 'SRH', 'DC', 'PBKS'],
    'team2': ['CSK', 'RCB', 'KKR', 'RR', 'DC', 'MI', 'PBKS', 'SRH'],
    'winner': ['MI', 'CSK', 'RCB', 'KKR', 'RR', 'MI', 'DC', 'SRH'],
    'total_runs': [195, 210, 185, 220, 175, 205, 190, 230]
})

print(data[(data['total_runs'] > 180) & data['total_runs'] < 220])
'''


