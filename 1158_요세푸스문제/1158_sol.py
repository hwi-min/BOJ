"""
rotate -> O(K)
popleft -> O(1)
"""
from collections import deque
N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
result = []

while queue:
    queue.rotate(-(K-1))
    result.append(queue.popleft())

# 출력
print("<", end='')
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end='')
    else: print(f"{result[i]},", end=' ')
print('>')

############################# 최적화 #############################
N, K = map(int, input().split())
queue = deque([i for i in range(1, N + 1)])
result = []

while queue:
    # K-1개를 뒤로 옮기기
    for _ in range(K-1):
        queue.append(queue.popleft())
    
    result.append(queue.popleft())

print(f"<{', '.join(map(str, result))}>")