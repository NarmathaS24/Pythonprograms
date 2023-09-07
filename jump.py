def min_jumps(nums):
    n = len(nums)
    min_jumps = [float('inf')] * n
    min_jumps[0] = 0

    for i in range(1, n):
        for j in range(i):
            if j + nums[j] >= i:
                min_jumps[i] = min(min_jumps[i], min_jumps[j] + 1)

    return min_jumps[n - 1]
nums = [2, 3, 1, 1, 4]
print(min_jumps(nums))