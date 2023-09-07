import numpy as np
a = np.array([10, 20, 30, 40, 50])
print("Original array:", a)
print("First element:", a[0])
print("Last element:", a[-1])
print("Slice of array:", a[1:3])
a[1] = 25
print("Array after modification:", a)
