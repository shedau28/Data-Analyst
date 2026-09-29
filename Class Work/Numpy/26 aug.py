import numpy as np

data = np.genfromtxt("numpy_dataset.csv", delimiter=",", skip_header=1)

base_price = data[:,2]
cost_price = data[:,6]
fmonth_units = data[:,3]
smonth_units = data[:,4]
tmonth_units = data[:,5]

first_rev = base_price*fmonth_units
second_rev = base_price*smonth_units
third_rev = base_price*tmonth_units

# print(first_rev)
# print(second_rev)
# print(third_rev)

f_total_rev = np.sum(first_rev)
# print("First month total revenue = ",f_total_rev)
s_total_rev = np.sum(second_rev)
# print("Second month total revenue = ", s_total_rev)
t_total_rev = np.sum(third_rev)
# print("Third month total revenue = ",t_total_rev)

total_rev = f_total_rev + s_total_rev + t_total_rev

# print("Total Revenue = ",total_rev)


first_month_cost = cost_price*fmonth_units
second_month_cost = cost_price*smonth_units
third_month_cost = cost_price*tmonth_units

first_month_total_cost = np.sum(first_month_cost)
second_month_total_cost = np.sum(second_month_cost)
third_month_total_cost = np.sum(third_month_cost)

f_total_prof = f_total_rev - first_month_total_cost
# print("First month total profit = ",f_total_prof)
s_total_prof = s_total_rev - second_month_total_cost
# print("Second month total profit = ",s_total_prof)
t_total_prof = t_total_rev - third_month_total_cost
# print("Third month total profit = ",t_total_prof)


total_profit = f_total_prof + s_total_prof + t_total_prof

# print("Total Profit = ",total_rev - total_profit)

# profit margin

first_month_profit_margin = (f_total_prof / f_total_rev) * 100 
second_month_profit_margin = (s_total_prof / s_total_rev) * 100 
third_month_profit_margin = (t_total_prof / t_total_rev) * 100 

# print(first_month_profit_margin)
# print(second_month_profit_margin)
# print(third_month_profit_margin)


cheapest_price_index = np.argmin(base_price)
costly_price_index= np.argmax(base_price)

cheapest_prod_price = base_price[cheapest_price_index]
costly_prod_price = base_price[costly_price_index]

# print(cheapest_prod_price)
# print(costly_prod_price)

# Average sales per month

total_products = fmonth_units.size
# print(total_products)

first_month_avg_sales = np.average(first_rev)
second_month_avg_sales = np.average(second_rev)
third_month_avg_sales = np.average(third_rev)
# print(first_month_avg_sales)
# print(second_month_avg_sales)
# print(third_month_avg_sales)


print(data[base_price > 500])





