n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
index_map = [()] * ((n * n) + 1)
# 8개의 인접한 좌표의 값을 확인하기 위한 directions
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

# 숫자 1부터 n*n까지의 좌표 저장
for row in range(n):
    for col in range(n):
        idx = grid[row][col]
        index_map[idx] = (row, col)

# 순서대로 탐색


