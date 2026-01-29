"""
dfs로 이어진 블럭 확인 -> ㅗ ㅏ ㅓ ㅜ 는 탐색 불가하니 별도 처리
완전 탐색 -> 500 * 500 = 250000
"""

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0 # 입력으로 주어지는 수가 1000을 넘지 않는 자연수이므로 초기 max를 0으로 초기화
visited = [[False] * M for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 4방향 정의

# 각 면이 이어져있는 모양 dfs 탐색
def dfs(r, c, depth, current_sum):
    global max_sum

    # break 조건
    if depth == 4: # 4칸 탐색을 마쳤다면 max_sum 업데이트 후 반환
        max_sum = max(max_sum, current_sum)
        return
    
    # 4방향 탐색
    for dx, dy in dir:
        nr, nc = r + dx, c + dy

        # 격자 내 범위에 있고 아직 방문하지 않았다면 방문
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, depth+1, current_sum+grid[nr][nc])
            visited[nr][nc] = False # 백트레킹

# ㅏ, ㅓ, ㅗ, ㅜ 탐색
def unique_shape(r, c):
    global max_sum
    is_available = []

    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            is_available.append(grid[nr][nc])

    is_available_len = len(is_available) # 갈 수 있는 곳의 개수

    if is_available_len < 3:
        return # 만들 수 있는 경우가 없으므로 반환
    
    if is_available_len == 3: # 가능한 곳이 3개면 모두 더하면 최대값
        max_sum = max(max_sum, grid[r][c] + sum(is_available))

    elif is_available_len == 4: # 가능한 곳이 4개면 최소 값 하나를 뺴고 모두 더한 값이 최대값
        max_sum = max(max_sum, grid[r][c] + sum(is_available) - min(is_available)) # 전체를 다 더해서 최소 값을 뺀게 최대 값이 됨

     

# main 실행부
for i in range(N):
    for j in range(M):
        visited[i][j] = True # 방문 체크
        dfs(i, j, 1, grid[i][j]) # dfs로 탐색
        visited[i][j] = False # 백트레킹

        unique_shape(i, j) # ㅏ, ㅓ, ㅗ, ㅜ 탐색

print(max_sum)
