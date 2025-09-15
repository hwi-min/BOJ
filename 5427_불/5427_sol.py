"""
시간제한: 1초(1억)
w, h <= 1000 / 최대 1000000 (백만)
"""
T = int(input())
for _ in range(T):
    w, h = map(int, input().split()) # w, h는 최대 1000
    building = [list(map(int, input().split())) for _ in range(h)]        
    
    # 불 시작점 찾기
    fire_x, fire_y = 0, 0
    # 상근이 시작 위치 찾기
    start_x, start_y = 0, 0

    # 시작점 찾으러 갑시다
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@': start_x, start_y = i, j
            elif building[i][j] == '*': fire_x, fire_y

    