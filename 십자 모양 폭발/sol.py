"""
시간제한 1초 -> 연산 1억
1 <= 숫자 <= 100
1 <= r, c <= N <= 200
"""
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1 # 인덱스 번호는 0부터 시작
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 방향 정의
cnt = grid[r][c] # 몇 번 터질지 정의
grid[r][c] = 0 # 터졌다는 의미로 0으로 변경

# 먼저 터지면 0으로 처리!
for i in range(1, cnt):
    for dx, dy in dir: # 사방으로 돌면서
        nr, nc = r + dx * i, c + dy * i
        if 0 <= nr < n and 0 <= nc < n: # grid 내에 존재하는 좌표라면?
            grid[nr][nc] = 0 # 터졌다는 뜻으로 0으로 변경

# 이제 0 제외후 떨어뜨리기
for row in range(n-1, -1, -1): # 아래에서 역으로 탐색
    for col in range(n-1, -1, -1):
        if grid[row][col] == 0: # 으로 터진 부분이라면
            zero_row, zero_col = row, col # 처리해야하는 부분을 저장함
            while 0 <= zero_row < row: # 0인 좌표보다 위에 존재하는 동안
                zero_row -= 1
                upper_elem = grid[zero_row][zero_col]
                if upper_elem != 0: # 해당 좌표가 0이 아닌 경우에는
                    grid[row][col] = upper_elem
                    grid[zero_row][zero_col] = 0
                    break # 바꾸고 더 이상 이동할 필요 없음 !

for row in grid:
    print(*row)
