from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for i in range(n)]
cnt = 0
nums = set()

for perm in permutations(cards, k):
    created = "".join(perm)
    if created not in nums:
        cnt += 1
        nums.add(created)

print(cnt)