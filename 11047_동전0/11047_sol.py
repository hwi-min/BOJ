N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
reversed_coins = sorted(coins, reverse=True)
total = 0

for coin in reversed_coins:
    # coin 보다 크면 skip
    if coin > K:
        continue
    
    # coin 보다 작으면
    left = K % coin
    total += K // coin

    K = left

print(total)

