import pandas as pd
data = {'Region': ['East', 'East', 'West', 'East', 'West', 'West'],
        'Manager': ['Narmatha', 'Narmatha', 'Jerome', 'Narmatha', 'Jerome', 'Jerome'],
        'Salesman': ['Varsha', 'Abigail', 'Jeni', 'Varsha', 'Jeni', 'Varsha'],
        'Sale_Amount': [2500, 3500, 4000, 2000, 3000, 4500]}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, values='Sale_Amount', index=['Region', 'Manager', 'Salesman'], aggfunc='sum')
print(pivot_table)

