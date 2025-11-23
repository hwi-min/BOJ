"""
Time Limit: 4초 -> 연산 약 4억
"""
from collections import Counter

mapper = {'L': 0, 'R': 1, 'U': 2, 'D': 3}
drs = [0, 0, -1, 1]
dcs = [-1, 1, 0, 0]

T = int(input())

for _ in range(T): # -> 최대 100
    N, M = map(int, input().split()) # N*N 격자에, M개의 구슬
    
    marbles = [] # (구슬의 r, 구슬의 c, 구슬의 방향(정수로))
    for _ in range(M): # -> 최대 2500
        xi, yi, di = input().split()
        xi, yi= int(xi), int(yi)
        marbles.append((xi-1, yi-1, mapper[di]))

    for _ in range(2*N):
        # 구슬 이동 or 방향 전환
        next_pos = {}

        for r, c, d in marbles: # 모든 구슬 돌면서
            nr, nc = r + drs[d], c + dcs[d]
            
            # 새 방향이 grid 이내이면 이동
            if 0 <= nr < N and 0 <= nc < N: 
                val = (nr, nc, d)
                key = (nr, nc)

            else: # 방향만 바꾸기
                if d == 1: opp = 0
                elif d == 0: opp = 1
                elif d == 2: opp = 3
                elif d == 3: opp = 2

                val = (r, c, opp)
                key = (r, c)

            # 방향이 next_pos에 아직 존재하지 않으면
            if key not in next_pos: # 생성
                next_pos[key] = []
            # 있으면 새 구슬의 위치 추가
            next_pos[key].append(val)

        new_marbles = []
        for items in next_pos.values():
            if len(items) == 1:
                new_marbles.append(items[0])

        marbles = new_marbles
        
        if not marbles:
            break

    print(len(marbles))