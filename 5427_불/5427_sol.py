"""
시간제한: 1초(1억)
w, h <= 1000 / 최대 1000000 (백만)
"""
from collections import deque
# 상하좌우 좌표
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def save_sanggeun(fire_queue):
    global visited

    while queue: # queue를 순회하면서
        current_x, current_y, current_time = fire_queue.popleft()

        # 인덱스 밖이라면? -> 탈출했습니다 !
        if current_x >= w or current_x < 0 or current_y >= h or current_y < 0:
            
        if building[current_x][current_y] == '.' and (current_x, current_y) not in visited and 

    

T = int(input())
for _ in range(T):
    w, h = map(int, input().split()) # w, h는 최대 1000

    # input 이중 리스트로 정리하기
    building = [] # buildling 정보 초기화
    for _ in range(h): # 높이 h를 돌면서
        h_elem = []
        h_elems = input() # input 받고
        for elem in h_elems: # 하나씩 돌면서 h_elem에 초가
            h_elem.append(elem)
        building.append(h_elem) # 다 돌면 h_elem을 buildling에 추가
    
    # 상근이 시작 위치 찾기
    start_x, start_y = 0, 0
    
    queue = deque() # 불 리스트
    fire_time = [[float('inf')] * w for _ in range(h)] # 불이 번지는 시간 리스트
    visited = set()

    # 상근이랑 불 찾으러 갑시다
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@': start_x, start_y = i, j
            elif building[i][j] == '*': 
                queue.append((i, j, 0)) # x좌표, y좌표, 시간
                visited.add((i, j)) # 방문했다는 것을 체크 미리해주기


    save_sanggeun


    