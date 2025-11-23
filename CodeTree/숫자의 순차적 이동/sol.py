n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
index_dict = {i:() for i in range(1, n*n+1)}

# 8개의 인접한 좌표의 값을 확인하기 위한 directions
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

# 숫자 1부터 n*n까지의 좌표 저장 -> N * N
for row in range(n):
    for col in range(n):
        idx = grid[row][col]
        index_dict[idx] = (row, col)

# m번의 턴을 돌면서 수행
for _ in range(m):
    # 순서대로 탐색 -> N * N
    for i in range(1, n*n+1):
        r, c = index_dict[i][0], index_dict[i][1] # 숫자 i의 r, c 불러오기
        max_num, max_r, max_c = -1, -1, -1 # 최고값, 최고값의 r, c 초기화
        origin_num = grid[r][c] # 원래 숫자 저장

        # 8칸을 모두 돌며
        for dx, dy in directions:
            nx, ny = r + dx, c + dy
            # 좌표 내에 존재한다면
            if 0 <= nx < n and 0 <= ny < n:
                current_num = grid[nx][ny] # 현재 숫자 저장
                if current_num > max_num:
                    max_num = current_num # 최고값 업데이트
                    max_r, max_c = nx, ny # 최고값의 인덱스 업데이트

        # 8개의 좌표를 모두 다 돌고 자리 바꾸기
        grid[r][c] = max_num
        grid[max_r][max_c] = origin_num

        # dict도 바꾸기
        index_dict[max_num] = (r, c)
        index_dict[origin_num] = (max_r, max_c)


for row in grid:
    print(*row)

