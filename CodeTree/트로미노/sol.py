"""
Time limit 1s(1000ms) -> 최대 연산 1억
3 <= N, M <= 200

최악의 경우 (N=200, M=200)일 때, 각 탐색의 연산 횟수

1. 1x3 (가로) 탐색: N * (M-2) 
   -> 200 * 198 = 39,600

2. 3x1 (세로) 탐색: (N-2) * M
   -> 198 * 200 = 39,600

3. 2x2 (L자 4종) 탐색: (N-1) * (M-1)
   -> 199 * 199 = 39,601

약 12만!!   
"""

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_sum = 0 # 음수가 없으므로 0으로 초기화

def checking_L(r, c):
    global grid
    sub_l, s1, s2, s3, s4 = 0, 0, 0, 0, 0

    sub_l += grid[r][c] + grid[r][c+1]
    
    if 0<= r-1 < n:
        s1 = sub_l + grid[r-1][c]
        s2 = sub_l + grid[r-1][c+1]
    
    if 0<= r+1 < n:
        s3 = sub_l + grid[r+1][c]
        s4 = sub_l + grid[r+1][c+1]

    sub_l = max(sub_l, s1, s2, s3, s4)

    return sub_l

# row 돌면서 1X3 탐색
for r in range(n):
    for c in range(m-2):
        sub_linear = grid[r][c] + grid[r][c+1] + grid[r][c+2]
        if sub_linear > max_sum: max_sum = sub_linear # max_sum보다 크다면 업데이트

# column 돌면서 1X3 탐색
for c in range(m):
    for r in range(n-2):
        sub_linear = grid[r][c] + grid[r+1][c] + grid[r+2][c]
        if sub_linear > max_sum: max_sum = sub_linear

# 4X4 grid 생성하며 L 블록 탐색
for r in range(n-1):
    for c in range(m-1): 
        total_sum = grid[r][c] + grid[r+1][c] + grid[r][c+1] + grid[r+1][c+1]

        s1 = total_sum - grid[r][c]
        s2 = total_sum - grid[r+1][c]
        s3 = total_sum - grid[r][c+1]
        s4 = total_sum - grid[r+1][c+1]
    
        max_sum = max(max_sum, s1, s2, s3, s4)

print(max_sum)