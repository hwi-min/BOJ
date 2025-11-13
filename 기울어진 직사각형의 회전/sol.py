"""
1초 -> 연산 1억
3 <= N <= 100
1 <= r, c <= N

"""
from collections import deque

def q_appending(start_r, start_c, position, cnt):
    global grid

    # dx, dy를 방향에 따라 설정
    if position == 1: dx, dy = -1, 1
    elif position == 2: dx, dy = -1, -1
    elif position == 3: dx, dy = 1, -1
    elif position == 4: dx, dy = 1, 1

    for i in range(cnt): # 주어진 횟수만큼 반복
        nx, ny = start_r + dx, start_c + dy
        if 0 <= nx < n and 0 <= ny < n: # grid index 범위 내일때만
           queue.append((grid[nx][ny])) # queue에 삽입 (값 자체)
           grid_queue.append((nx, ny)) # 좌표 저장




n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# 초기 시작 요소 큐에 삽입
queue = deque([(grid[r][c])])
grid_queue = deque([(r, c)])

# 1번 위치로 이동
q_appending(r, c, 1, m1)
# 2번 위치로 이동
q_appending(r, c, 2, m2)
# 3번 위치로 이동
q_appending(r, c, 3, m3)
# 4번 위치로 이동
q_appending(r, c, 4, m4)

# 시계 방향
if dir == 1:queue.rotate(1) # 시계 방향
elif dir == 0: queue.rotate(-1) # 반시계 방향

while queue:
    r, c = grid_queue.popleft()
    elem = queue.popleft()
    grid[r][c] = elem

for row in grid:
    print(*row)