"""
시간제한: 1초 (1억)
M, N, H는 모두 100 이하
1: 익은 토마토
0: 익지 않은 토마토
-1: 토마토가 없는 칸

최악의 경우: 100 * 100 * 100 = 1000000 (백만)
-> 이 리스트 완탐한다? 백만임

## 제일 아래부터 탐색하면, 아래 박스는 고려할 필요가 없음! -> 맞음?
초기에 for문 돌때, total 변수를 만들어 두고, 1이 있는 경우 + 1해, 그리고 토마토 익을때마다 +1해
그리고 queue다 돌았는데? total이 M*N*H보다 작으면 -1, 같으면 최소 일수
그리고 queue 안에 종료조건 넣어 total이 M*N*H가 되면 바로 break하고 현재 날짜 출력!
"""
from collections import deque

# 방향         박스 내 위   박스 내 아래  박스 내 오른쪽 박스 내 왼쪽    박스 아래     박스 위
direction = [(0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0 ,-1), (-1, 0, 0), (1, 0, 0)]

def are_tomatoes_ripe(ripen_tomatoes):
    global total
    
    spent_day = 0
    while ripen_tomatoes:
        h, x, y, day = ripen_tomatoes.popleft()
        spent_day = day 

        # if total == max_tomates: -> 여기 있으면 안됨 왜냐면 queue에 넣을 때 total += 1을 한거니까 다 돌아봐야함
        #     return day

        for dh, dx, dy in direction:
            nh, nx, ny = h + dh, x + dx, y + dy
            # 유효 인덱스 안에 존재하고, 토마토가 존재하면?
            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and tomatoes[nh][nx][ny] == 0:
                tomatoes[nh][nx][ny] = 1
                ripen_tomatoes.append((nh, nx, ny, day+1))
                total += 1 # 토마토 익었어용 ~ 표시 -> 큐에 넣을때 !!! 더하는거임 !!

    if total == max_tomates: return spent_day
    return -1 # queue를 다 돌았는데, 전체 토마토가 익지 않았다면? 다 못익습니다! -> -1 출력

M, N, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
max_tomates = N*H*M # 최대 토마토는 전체 칸에 다 토마토가 있는 경우
total = 0
queue = deque()

# 0일차에 익어있는 토마토 정보를 모두 queue에 삽입
for h in range(H): # 아래 층부터
    for i in range(N): # 행
        for j in range(M): # 열
            if tomatoes[h][i][j] == 1:
                queue.append((h, i, j, 0))
                total += 1 # 익은 토마토니까 1 추가합니당
            elif tomatoes[h][i][j] == -1:
                max_tomates -= 1

if total == max_tomates: min_day = 0 # 이미 최대 토마토수와 현재 토마토 수가 같으면 탐색 안 해도 됨!
else: min_day = are_tomatoes_ripe(queue)

print(min_day)