n, m, k = map(int, input().split()) # N: 격자 크기 / M: 블록크기 / K: 위치 정보
grid = [list(map(int, input().split())) for _ in range(n)]
k -= 1 # 0-based index
valid_row = -1 # 초기 row -1로 초기화

for row in range(n):
    if grid[row][k] == 0: # 해당 위치에 갈 수 있다면?
        flag = True
        for s in range(1, m):
            nc = k + s
            if not flag: # 이미 불가능하다는 플래그가 있으면 해당 위치는 올 수 없으므로 탈출
                break 
            if grid[row][nc] == 1: # 둘 수 없는 위치가 있다면
                flag = False # flag 표시하고
                break 
        if flag: # flag가 여전히 true이면 해당 row에 둘 수 있음
            valid_row = row
        else: # 이번 행이 안되면 더 이상 밑으로 안내려감
            break
    else: # 첫 시작점도 갈 수 없다면
        break
        
        
if valid_row != -1:
    for s in range(m):
        grid[valid_row][k+s] = 1

for row in grid:
    print(*row)
