import numpy as np
import random

np.random.seed(123)

# number of products
n_prod = 10

# BasePrice
base_price = np.random.randint(500, 1500, size=n_prod).astype(float)
# print(base_price)

# 1st month units
first_mon_units = np.random.randint(20, 100, size=n_prod).astype(float)

# 2nd month units
second_mon_units = np.random.randint(20, 100, size=n_prod).astype(float)

# 3rd month units
third_mon_units = np.random.randint(20, 100, size=n_prod).astype(float)

# cost price
cost_per = np.random.uniform(0.4, 0.7, size=n_prod)
# print(cost_per)

cost_price = base_price * cost_per
# print(cost_price)

# revenue
first_rev = base_price*first_mon_units
second_rev = base_price*second_mon_units
third_rev = base_price*third_mon_units

first_total_rev = np.sum(first_rev)
second_total_rev = np.sum(second_rev)
third_total_rev = np.sum(third_rev)

total_rev = first_total_rev + second_total_rev + third_total_rev

# print(first_total_rev)
# print(second_total_rev)
# print(third_total_rev)
# print(total_rev)

# profit
first_cost = cost_price*first_mon_units
second_cost = cost_price*second_mon_units
third_cost = cost_price*third_mon_units

first_total_cost =np.sum(first_cost)
second_total_cost =np.sum(second_cost)
third_total_cost =np.sum(third_cost)

total_cost = first_total_cost + second_total_cost + third_total_cost

first_prof = first_total_rev - first_total_cost
second_prof = second_total_rev - second_total_cost
third_prof = third_total_rev - third_total_cost

total_prof = first_prof + second_prof + third_prof

print(first_prof)
print(second_prof)
print(third_prof)
print(total_prof)