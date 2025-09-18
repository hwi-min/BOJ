"""
제한시간: 2초 (2억)
- n, m은 500이하
- 모든 노드는 250000 (25만)
"""
from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_word(x, y):
    visited.add((x, y))
    queue = deque([(x, y)]) # 정점 하나당 bfs를 실행해야하니까
    area = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            # 왼쪽부터 조건 검사를 하기 때문에 인덱스 확인을 가장 먼저 작성해야함 !!
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and paper[nx][ny] == 1:
                queue.append((nx, ny))
                visited.add((nx, ny))
                area += 1

    return area



n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = set() # visited 초기화
# work = set() # 작품 셋 -> 필요 없을 듯 그냥 visited가 이미 된 애는 탐색 안 하면 돼
max_size = 0
work_cnt = 0

for i in range(n):
    for j in range(m):
        # 1인 해당 정점을 시작 (단 이미 방문했으면 갈 필요 없음)
        if (i, j) not in visited and paper[i][j] == 1:
            work_cnt += 1
            current_dist = find_word(i, j)
            if current_dist > max_size: max_size = current_dist

print(work_cnt)
print(max_size)