numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_numbers = list(map(lambda x: x**2, numbers))
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(even_numbers)
print(squared_numbers)
print(product)
