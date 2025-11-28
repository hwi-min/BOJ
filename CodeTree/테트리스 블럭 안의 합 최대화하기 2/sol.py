from itertools import combinations

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 인접한 방향 탐색
max_sum = float('-inf')
visited = [[False] * M for _ in range(N)]

# 해당 r, c를 중심 위치로 보고 수행
# def check_exception(r, c):
#     global max_sum
#     central_val = grid[r][c]

#     # 1. 유효 이웃 찾기
#     neighbors = []
#     for dx, dy in dir:
#         nr, nc = r + dx, c + dy
#         if 0 <= nr < N and 0 <= nc < M:
#             neighbors.append((nr, nc))
    
#     neighbors_cnt = len(neighbors)

#     # 인접한 칸이 3개 미만이면 T자 못 만듦
#     if neighbors_cnt < 3:
#         return
    
#     # 3개 이상이면 
#     for three_neighbors in combinations(neighbors, 3):
#         base_sum = central_val
#         # T자모양 확인
#         for nr, nc in three_neighbors:
#             base_sum += grid[nr][nc]
#     for i in range(neighbors_cnt):
#         if neighbors_cnt == 3 and i > 0: 
    


def dfs(r, c, current_sum, selected_nums): # 좌표의 r, c, 현재까지의 합, 선택된 숫자의 개수
    global max_sum

    # 종료 조건
    if selected_nums == 5: # 숫자를 5개 선택한 경우
        if max_sum < current_sum: # 현재까지의 합이 더 크다면 업데이트
            max_sum = current_sum
        return # 반환
    
    for dx, dy in dir: # 인접한 4방향을 모두 돌며
        nr, nc = r + dx, c + dy
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]: # grid 이내에 존재하고, 아직 방문하지 않은 곳이라면
            visited[nr][nc] = True # 방문 체크
            dfs(nr, nc, current_sum+grid[nr][nc], selected_nums+1) # 재귀로 탐색
            # backtracking
            visited[nr][nc] = False # 재귀 탐색 후에는 다시 갈 수 있도록 방문 체크 해제
    
### 실행부 ### 
# -> 완전탐색
for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r, c, grid[r][c], 1) # r, c, 현재까지 합, 선택 개수
        check_exception(r, c)

print(max_sum)

