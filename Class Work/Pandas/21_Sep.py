import pandas as pd
import matplotlib.pyplot as plt

# data = {
#     "Employee": ["Amit", "Rahul", "Priya", "Neha", "Vikas",
#                  "Sneha", "Rohan", "Pooja", "Karan", "Anita",
#                  "Raj", "Meena"],

#     "Salary": [25000, 28000, 30000, 32000, 35000, 36000,
#                38000, 40000, 42000, 45000, 48000, 300000],

#     "Experience": [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 15],

#     "Age": [22, 24, 25, 26, 28, 29, 30, 31, 33, 35, 38, 55]
# }


# df = pd.DataFrame(data)
# print(df)
# print(df['Salary'].describe())

# q1 = df["Salary"].quantile(0.25)
# q2 = df["Salary"].quantile(0.5)
# q3 = df["Salary"].quantile(0.75)

# print(f"Quarter 1 = {q1}")
# print(f"Quarter 2 = {q2}")
# print(f"Quarter 3 = {q3}")

# iqr = q3 - q1

# print(f"IQR = {iqr}")

# lower_bound = q1 - 1.5*iqr
# upper_bound = q3 + 1.5*iqr

# print(f"Lower Bound is : {lower_bound}")
# print(f"Upper Bound is : {upper_bound}")


# outlier = df[(df["Salary"]<lower_bound) | (df["Salary"]>upper_bound)]
# print(f"{outlier}")

# count_out = ((df["Salary"]<lower_bound) | (df["Salary"]>upper_bound)).sum()
# print(f"Count Outliers : {count_out}")


# df["Salary_Outlier"] = (
#     (df["Salary"] < lower_bound) |
#     (df["Salary"] > upper_bound)
# ).astype(int)

# print(df)


# df_clean = df[
#     (df["Salary"] >= lower_bound) &
#     (df["Salary"] <= upper_bound)
# ]

# print(df_clean)

# removed = len(df) - len(df_clean)

# print("Outliers removed:", removed)


# df["Salary_Capped"] = df["Salary"].clip(
#     lower=lower_bound,
#     upper=upper_bound
# )

# print(df)


data = {
    "Employee": ["Amit", "Rahul", "Priya", "Neha", "Vikas",
                 "Sneha", "Rohan", "Pooja", "Karan", "Anita",
                 "Raj", "Meena"],

    "Salary": [25000, 28000, 30000, 32000, 35000, 36000,
               38000, 40000, 42000, 45000, 48000, 300000],

    "Experience": [1, 15, 2, 3, 4, 4, 5, 6, 7, 8, 9, 2],

    "Age": [22, 24, 35, 26, 55, 28, 30, 31, 33, 35, 28, 28]
}


# Detect an outlier in Experience

df = pd.DataFrame(data)

# q1 = df["Experience"].quantile(0.25)
# q2 = df["Experience"].quantile(0.5)
# q3 = df["Experience"].quantile(0.75)

# print(f"Q1 : {q1}")
# print(f"Q2 : {q2}")
# print(f"Q3 : {q3}")

# iqr = q3 - q1

# lower_bound = q1 - 1.5*iqr
# upper_bound = q3 + 1.5*iqr

# print(f"Lower Bound : {lower_bound}")
# print(f"Upper Bound : {upper_bound}")

# outlier = df[(df["Experience"] < lower_bound) | (df["Experience"] > upper_bound)]
# print("Outlier Found : ")
# print(outlier['Experience'])

# count_outlier = ((df["Experience"] < lower_bound) | (df["Experience"] > upper_bound)).sum()
# print(f"Total Outliers Found : {count_outlier}")

# df["outlier"] = ((df["Experience"] < lower_bound) | (df["Experience"] > upper_bound))
# print(df)

# df_clean = df[(df["Experience"] >= lower_bound) & (df["Experience"] <= upper_bound)]
# print(df_clean)



def find_outlier(df, column):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - 1.5*iqr
    upper_bound = q3 + 1.5*iqr

    outlier = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    box_plot =df.boxplot(column=column)
    plt.show()
    return outlier


# age_out = find_outlier(df, "Age")
# print(age_out)
# salary_out = find_outlier(df, "Salary")
# print(salary_out)
# exp_out = find_outlier(df, "Experience")
# print(exp_out)

# duplicate : 

dups = df.duplicated(subset=['Age'])
print(dups)

rem_dups = df.drop_duplicates(subset=['Age'])
print(rem_dups)


"""
result  =df.duplicated(subset=['Price'])
print(result)
"""
# drop_duplicates :

"""
df = df.drop_duplicates(subset=['Price'])
print(df)

result =df.duplicated(subset=['Price']).sum()
print(result)
"""

# new col  :  revenue = price * qty

# df['revenue'] = df['Price'] * df['Qty']
# print(df)

# discount  : 

"""def discount_revenue(revenue):
    if revenue > 50000 :
        return revenue * 0.1
    else :
        return revenue * 0.05
    
df['discount'] =df['revenue'].apply(discount_revenue)
print(df)"""

