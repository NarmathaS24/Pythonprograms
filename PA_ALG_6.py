def coin_change_ways(coins, N):
    ways = [0] * (N + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, N + 1):
            ways[i] += ways[i - coin]
    return ways[N]
coins = [1, 2, 5]
N = 10
num_ways = coin_change_ways(coins, N)
print(num_ways)
