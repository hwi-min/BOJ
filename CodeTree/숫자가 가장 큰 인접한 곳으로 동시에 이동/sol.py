n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 -> 하 -> 좌 -> 우
marbles = []

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r -1, c- 1
    marbles.append((r, c)) # 초기 좌표 queue에 삽입

for time in range(t): # 0 ~ t 시점까지
    move_grid = [[0] * n for _ in range(n)]

    for r, c in marbles: # 전체 구슬을 돌면서
        find_max = -1
        ux, uy = -1, -1

        # 모든 방향을 탐색하며
        for dx, dy in directions:
            nx, ny = r + dx, c + dy
            # 범위 내에 존재하고, 해당 값이 find_max의 현재값보다 큰 경우에 업데이트 (우선순위 적용)
            if 0 <= nx < n and 0 <= ny < n:
                cur_num = grid[nx][ny]
                if find_max < cur_num: 
                    find_max = cur_num
                    ux, uy = nx, ny

        # ux, uy가 -1이 아니고 업데이트가 되었다면? -> 개수를 세는 move_grid에 숫자 추가
        if ux != -1 and uy != -1: move_grid[ux][uy] += 1 

    # 이제 1개만 있는 위치 저장
    new_marbles = []
    for row in range(n):
        for col in range(n):
            if move_grid[row][col] == 1:
                new_marbles.append((row, col))

    marbles = new_marbles

print(len(marbles))