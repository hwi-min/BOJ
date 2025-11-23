"""
1 <= r, c <= N <= 100
1초 -> 1억

"""

n, r, c = map(int, input().split())
a = [list(map(int ,input().split())) for _ in range(n)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우 (우선순위 기반)
r, c = r-1, c-1 # 0-based index
result = [a[r][c]]
visited = set()
visited.add((r, c))


while True:
    is_found = False
    for dx, dy in dir:
        nx, ny = r + dx, c + dy # 새로운 nx, dy 선언
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > a[r][c] and a[nx][ny] not in visited: # grid 내부에 있고, 현재 숫자보다 큰 경우
            r, c = nx, ny # r, c 업데이트
            visited.add((r, c))
            is_found = True # 이동했다는 표시 
            result.append(a[r][c])
            break # 우선순위에 따라 먼저 발견하면 그만 탐색하면 됨

    if not is_found: # 큰 숫자가 없어서 이동하지 못했다면
        break # 그만 탐색하고 탈출

print(*result)
