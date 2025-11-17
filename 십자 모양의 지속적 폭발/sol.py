"""
시간 제한 1초 -> 1억
1 <= c <= N <= 200
1 <= M <= 10
"""

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# commands의 횟수만큼 반복 
for i in range(m): 
    column = commands[i] - 1 # 인덱스는 0부터 시작하므로
    is_found = False
    ## 폭탄이 터지는 부분 0으로 처리
    # bomb_cnt 찾기 
    for j in range(n): # 0이 아닌 시작점 찾기
        if is_found: break # 이미 0이 아닌 시작점 찾으면 break

        if grid[j][column] != 0: # 0이 아닌 시작점 찾았다면
            bomb_cnt = grid[j][column] # cnt 선언하고
            grid[j][column] = 0 # 터짐 처리
            is_found = True # 찾았다는 flag
            r, c = j, column


    for l in range(1, bomb_cnt): 
        for dx, dy in dir:
            nx, ny = r + dx * l, c + dy * l
            if 0 <= nx < n and 0 <= ny < n: # grid 이내의 인덱스라면
                grid[nx][ny] = 0 # 터졌다는 표시!
    
    ## 터진 폭탄 처리하고 grid 재구성
    for j in range(n):
        col = [grid[i][j] for i in range(n) if grid[i][j] != 0]

        for i in range(n):
            grid[i][j] = 0
        
        for idx, val in enumerate(col[::-1]):
            grid[n-1-idx][j] = val


for row in grid:
    print(*row)

        
