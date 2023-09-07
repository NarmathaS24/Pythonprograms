d = {'a': 3, 'b': 1, 'c': 2}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
sorted_d_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print('Original dictionary:', d)
print('Dictionary sorted by value (ascending):', sorted_d)
print('Dictionary sorted by value (descending):', sorted_d_desc)
