"""
제한시간: 2초 (2억)
- n, m은 500이하
- 모든 노드는 250000 (25만)
"""
from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_word(x, y, dist):
    visited.add((x, y))
    queue = deque([(x, y, dist)]) # 정점 하나당 bfs를 실행해야하니까


    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (n-1, m-1):
            return dist
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if (nx, ny) not in visited and paper[nx][ny] == 1 and 0 <= nx < n and 0 <= ny < m:
                queue.append((nx, ny, dist+1))
                visited.add((nx, ny))
    return False



n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = set() # visited 초기화
work = set() # 작품 셋 -> 필요 없을 듯 그냥 visited가 이미 된 애는 탐색 안 하면 돼
max_size = 0
print(paper)
for i in range(n):
    for j in range(m):
        # 1인 해당 정점을 시작 (단 이미 방문했으면 갈 필요 없음)
        if (i, j) not in visited and paper[i][j] == 1:
            current_dist = find_word(i, j, 1)
            if current_dist and current_dist > max_size:
                max_size = current_dist

print(max_size)