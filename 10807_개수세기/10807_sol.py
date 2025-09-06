"""
시간제한: 1초(1억/10**8)
"""

N = int(input())
nums = list(map(int, input().split()))
find = int(input())
cnt = 0

for num in nums:
    if num == find:
        cnt += 1

print(cnt)
