def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return (True, i)
    return (False, -1)
# Test the function
arr = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
x = 31
found, index = linear_search(arr, x)
if found:
    print(f"{x} found at index {index}")
else:
    print(f"{x} not found")
