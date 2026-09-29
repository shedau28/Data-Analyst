import pandas as pd
import numpy as np

df =pd.DataFrame({
    "id" :[1,2,3,4,5,6,7],
    'name' : ["ram","sita","ravan","bhudev","sahdev","minaxi","yug"],
    "age" :[56,25,np.nan,41,np.nan,23,np.nan],
    "salary":[10000,20000,np.nan,8580,np.nan,96000,np.nan]
})
print(df)

# df = df.dropna(axis=1)
df = df.dropna(axis=0)
print(df)


