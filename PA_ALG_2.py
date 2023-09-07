def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Iterate over each pair of adjacent elements and swap them if they are in the wrong order
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Test the function
a = [12, 5, 7, 18, 11, 6, 12, 4, 17, 1]
bubble_sort(a)
print(a)
