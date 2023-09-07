import pandas as pd
dict1 = {'name': ['Jerome', 'Narmu', 'Jack'],
         'age': [22, 19, 28],
         'city': ['India', 'UK', 'US']}
dict2 = {'name': ['Anu', 'Gopi', 'Vicky'],
         'age': [32, 27, 29],
         'city': ['Los Angeles', 'Boston', 'Chicago']}
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df = pd.concat([df1, df2], ignore_index=True)
print(df)
