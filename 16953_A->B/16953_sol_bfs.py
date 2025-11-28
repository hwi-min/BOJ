# bfs
from collections import deque

A, B = map(int, input().split())
visited = set()
queue = deque([(A, 1)])
result = -1

while queue:
    curr_num, cnt = queue.popleft()

    if curr_num > B:
        continue

    if curr_num == B:
        result = cnt
        break

    if curr_num * 2 not in visited:
        queue.append((curr_num*2, cnt +1))
        visited.add(curr_num*2)

    if curr_num * 10 + 1 not in visited:
        queue.append((curr_num*10+1, cnt +1))
        visited.add(curr_num*10+1)

print(result)