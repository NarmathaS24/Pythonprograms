import pandas as pd
df = pd.DataFrame({'name': ['Jerome', 'Narmatha', 'Abigail', 'Keerthu'],
                   'favorite_color': ['blue', 'green', 'yellow', 'orange']})
print("Original DataFrame:")
print(df)
def remove_repetitive_chars(s):
    return ''.join(sorted(set(s), key=s.index))
df['name'] = df['name'].apply(remove_repetitive_chars)
print("Updated DataFrame:")
print(df)
