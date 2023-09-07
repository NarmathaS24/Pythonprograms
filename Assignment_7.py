rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of columns:"))
print("Enter the matrix elements:")
matrix=[[int(input()) for i in range(cols)] for j in range(rows)]
print("Matrix elements:")
for i in range(rows):
    for j in range(cols):
        print(" ",(format(matrix[i][j])),end="")
    print()
res=[[int(0) for i in range(rows)]for j in range(cols)]
print("\nTransposed Matrix:")
for i in range(cols):
    for j in range(rows):
        res[i][j]=matrix[j][i]
        print(" ",format((res[i][j])),end="")
    print()



















"""8.1"""
import numpy as np
x = np.arange(12).reshape((2, 6))
print("\nOriginal array:")
print(x)
r1 = np.ptp(x, 1)
r2 = np.amax(x, 1) - np.amin(x, 1)
assert np.allclose(r1, r2)
print("\nDifference between the maximum and the minimum values of the said array:")
print(r1)
#8.2
import pandas as pd
s = pd.date_range('2023-02-19', periods=12, freq='BM')
df = pd.DataFrame(s, columns=['Date'])
print('last working days of each month of a specific year:')
print(df)
