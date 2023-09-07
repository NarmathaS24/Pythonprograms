def selection_sort(data):
    for i in range(len(data)):
        # Find the index of the smallest element in the unsorted part of the array
        min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        # Swap the smallest element with the first element in the unsorted part of the array
        data[i], data[min_index] = data[min_index], data[i]

# Test the function
data = [14, 46, 43, 27, 57, 41, 45, 21, 70]
selection_sort(data)
print(data)
