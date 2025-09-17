"""
시간 제한: 1초 (1억)
N, M은 100이하 
-> 모든 노드는 N*M 최대 10000(1만)
-> 한 노드에서
    1. popleft() : O(1)
    2. visited 추가: O(1)
    3. 도착점인지 확인 
    4. 4방향 확인
    5. ... 등 모두 상수 계산
    -> 만약 20~30의 연산이라고 한다해도 최대 연산 20만이므로 넉넉함!
"""
from collections import deque

N, M = map(int, input().split())
maze = [[int(char) for char in input()]for _ in range(N)]

# 시작점 설정
start_x, start_y = 0, 0
# queue 초기화, visited 초기화
queue = deque([(start_x, start_y, 0)]) # x, y, dist
visited = set()
# visited.add((start_x, start_y)) # 첫 위치 방문 체크
min_dist = float('inf')

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

while queue:
    x, y, dist = queue.popleft()
    visited.add((x, y)) # 체크 필요

    # 도착점에 도착했다면?
    if (x, y) == (N-1, M-1): 
        if min_dist > dist: 
            min_dist = dist # 지금거리가 최소 거리라면 min_dist 업데이트
            break # 탐색 그만 !

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        # 범위 내에 있고, 아직 방문하지 않았다면
        if (nx, ny) not in visited and 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
            queue.append((nx, ny, dist+1))
            visited.add((nx, ny))

# 첫 시작점도 포함이니까
print(min_dist+1)