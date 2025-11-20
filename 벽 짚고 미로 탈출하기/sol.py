import sys

# 입력 받기
N = int(input())
x, y = map(int, input().split())
x, y = x - 1, y - 1 # 0-based index로 변환

grid = [list(input()) for _ in range(N)]

# 방향: 우(0), 상(1), 좌(2), 하(3) (반시계 방향 배치)
# 이렇게 배치하면 (idx - 1)은 시계방향(오른쪽), (idx + 1)은 반시계방향(왼쪽)이 됩니다.
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
curr_dir = 0 
time = 0 # 변수명 통일 (t -> time)

# 방문 체크: (x좌표, y좌표, 방향)을 모두 기록해야 함
visited = set()
visited.add((x, y, curr_dir))

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

while True:
    # 1. 현재 나를 기준으로 '오른쪽' 좌표 계산
    right_dir = (curr_dir - 1) % 4
    rx, ry = x + directions[right_dir][0], y + directions[right_dir][1]

    # [우선순위 1] 오른쪽에 벽이 없다면? (오른쪽으로 회전 + 1칸 전진)
    # 격자 밖으로 나가는 경우도 '벽이 없는 것'으로 간주하여 탈출 시도
    if not in_range(rx, ry) or grid[rx][ry] == '.':
        curr_dir = right_dir # 방향 회전
        x, y = rx, ry        # 이동
        time += 1
    
    # [우선순위 2] 오른쪽에 벽이 있다면? (현재 방향으로 직진 시도)
    else:
        fx, fy = x + directions[curr_dir][0], y + directions[curr_dir][1]

        # 앞이 비어있거나 격자 밖이라면 -> 직진
        if not in_range(fx, fy) or grid[fx][fy] == '.':
            x, y = fx, fy
            time += 1
        
        # [우선순위 3] 오른쪽도 벽이고, 앞도 벽이라면 -> 왼쪽으로 회전 (이동 X)
        else:
            curr_dir = (curr_dir + 1) % 4
            time += 1
    
    # --- 이동 후 체크 ---

    # 1. 탈출 성공 확인 (격자 밖으로 나갔는지)
    if not in_range(x, y):
        print(time)
        break

    # 2. 무한 루프 확인 (같은 위치, 같은 방향으로 다시 왔는지)
    if (x, y, curr_dir) in visited:
        print(-1)
        break

    # 방문 기록
    visited.add((x, y, curr_dir))