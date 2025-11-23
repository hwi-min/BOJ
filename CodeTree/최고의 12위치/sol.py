"""
Time Limit: 5초 -> 약 연산 5억
완전탐색 -> 방문 체크 -> 재귀 -> 복구
백트래킹

"""

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
max_coins = 0

def can_place(r, c, dr, dc):
    # r, c 위치에서 시작해서 dr, dc 방향으로 타일을 놓을 수 있는지 체크
    # - 격자를 벗어나면 안되고
    # - 두 칸 모두 아직 사용하지 않았어야함
    nr, nc = r + dr, c + dc
    if nr >= N or nc >= N:
        return False
    
    if visited[r][c] or visited[nr][nc]:
        return False

    return True

def dfs(r, c, placed_count, total_coins): # 현재 r위치, 현재 c 위치, 지금까지 놓은 타일 수, 지금까지 획득한 동전 수
    global max_coins

    # K개 다 놓았으면 최댓값 갱신
    if placed_count == K: 
        if total_coins > max_coins: max_coins = total_coins
        return
    
    # 모든 행을 다 봤으면 종료
    if r == N:
        return
    
    # 다음 칸 좌표 계산 (같은 행에서 오른쪽 한 칸 이동)
    next_r, next_c = r, c + 1 
    if next_c == N: # 만약 열 끝에 도달했다면 
        next_r = r + 1 # 다음 행으로 넘기고
        next_c = 0 # 열은 가장 앞으로

    if visited[r][c]: # 현재 칸이 이미 다른 타일로 덮여있으면 다음 칸 이동
        dfs(next_r, next_c, placed_count, total_coins)
        return
    
    # 가로 타일 놓기 (1*2 타일)
    if can_place(r, c, 0, 1):
        visited[r][c] = True
        visited[r][c+1] = True

        coins = grid[r][c] + grid[r][c+1]

        # 다음 칸 진행
        dfs(next_r, next_c, placed_count+1, total_coins+coins)

        # backtracking -> 다른 경우의 수 시도를 위해
        visited[r][c] = False
        visited[r][c+1] = False

    if can_place(r, c, 1, 0):
        visited[r+1][c] = True
        visited[r][c] = True

        coins = grid[r][c] + grid[r+1][c]

        dfs(next_r, next_c, placed_count+1, total_coins+coins)

        # backtracking -> 다른 경우의 수 시도를 위해
        visited[r][c] = False
        visited[r+1][c] = False

    # 현재 칸에 놓지 않고 넘어가기
    dfs(next_r, next_c, placed_count, total_coins)

dfs(0, 0, 0, 0)
print(max_coins)