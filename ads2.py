def fibonacci_range(start, end):
    fib_series = [0, 1]
    while fib_series[-1] < end:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return [x for x in fib_series if x >= start and x <= end]
fibonacci_series = fibonacci_range(0, 100)
print(fibonacci_series)
