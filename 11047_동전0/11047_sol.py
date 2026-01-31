"""
1. 청소되어있지 않으면 청소
2. 현재 칸의 4방향 중 청소할 곳 없으면
    2-1. 뒤로 한칸 후진 -> 1번으로 돌아감
3. 현재 칸의 4방향 중 청소 할 곳있으면
    3-1. 반시계 방향으로 90도 회전
    3-2. 바라보는 방향 기준 청소 해야하면 한 칸 전진
    3. 1번으로 돌아감
"""

N, M = map(int, input().split()) # 3 <= N, M <= 50
r, c, d = map(int, input().split()) # 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
room = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서
visited = set() # 방문한 좌표 저장하는 집합 (초기 청소기 칸은 무조건 청소하니까)
cnt = 0 # 청소한 구역 초기화(청소기가 있는 구역은 무조건 빈칸이니까)

# 0 -> 청소해야 함
# 1 -> 벽이 있음

def lets_clean(r, c, d):
    global cnt

    # 1. 현재 칸이 청소되지 않은 경우 청소
    if (r, c) not in visited:
        visited.add((r, c))
        cnt += 1

    # 2. 현재 칸 주변 4방향 확인
    is_available = False
    for i in range(4):
        nr, nc = r + dir[i][0], c + dir[i][1]
        if 0 <= nr < N and 0 <= nc < M:
            if room[nr][nc] == 0 and (nr, nc) not in visited:
                is_available = True
                break

    # 3. 청소 할 곳이 없는 경우 (후진 로직)
    if not is_available:
        # 현재 바라보는 방향 d의 반대 방향으로 후진
        # 북(0)->남(2), 동(1)->서(3), 남(2)->북(0), 서(3)->동(1)
        back_idx = (d + 2) % 4
        rr, cc = r + dir[back_idx][0], c + dir[back_idx][1]
        
        # 뒤쪽이 벽이 아니면 후진 (방향 d는 유지)
        if 0 <= rr < N and 0 <= cc < M and room[rr][cc] != 1:
            lets_clean(rr, cc, d)
        else:
            return # 후진 불가능하면 종료

    # 4. 청소 할 곳이 있는 경우 (회전 및 전진)
    else:
        # 3-1. 반시계 방향으로 90도 회전
        d = (d + 3) % 4 
        nr, nc = r + dir[d][0], c + dir[d][1]
        
        # 3-2. 바라보는 방향 앞쪽 칸이 청소되지 않은 빈칸인 경우 한 칸 전진
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0 and (nr, nc) not in visited:
            lets_clean(nr, nc, d)
        else:
            # 청소할 곳이 생길 때까지 회전하며 1번으로 돌아감
            lets_clean(r, c, d)

## 실행부
lets_clean(r, c, d)
print(cnt)