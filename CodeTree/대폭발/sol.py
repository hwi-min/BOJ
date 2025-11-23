n, m, r, c = map(int, input().split())
grid = [[0] * n for _ in range(n)] # 빈 grid 생성
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 방향 -> 4방향
r, c = r-1, c-1 # 0-based index
bombs = [(r, c)]
grid[r][c] = 1 # 초기 폭탄 존재 체크
cnt = 0

for t in range(1, m+1): # 시간은 1~m초까지!
    new_bombs = [] # 새 폭탄 저장
    for br, bc in bombs:
        for dx, dy in directions:
            nx, ny = br + (dx * 2**(t-1)), bc + (dy * 2**(t-1))

            # grid가 인덱스 이내에 존재하고 + 아직 폭탄이 없다면
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0: 
                grid[nx][ny] = 1
                new_bombs.append((nx, ny))

    bombs.extend(new_bombs)
                
                    
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            cnt += 1

print(cnt)