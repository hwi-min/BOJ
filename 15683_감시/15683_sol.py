"""
시간 제한 1초: 연산 1억

cctv 위치별로 최적의 조합을 찾아야 함
dfs로 완전탐색하면 됨 

4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0

"""
from collections import deque
import copy

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
        # 상,      하,      좌,      우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
mode = [
        [],
        [[0], [1], [2], [3]], # 1번 CCTV: 상, 하, 좌, 우  방향으로 갈 수 있음
        [[0, 1], [2, 3]],     # 2번 CCTV: (상, 하), (좌, 우) 방향으로 갈 수 있음
        [[0, 2], [0, 3], [1, 2], [1, 3]], # 3번 CCTV: (상, 좌), (상, 우), (하, 좌), (하, 우) 방향으로 갈 수 있음
        [[0, 2, 3], [1, 2, 3], [0, 1, 2], [0, 1, 3]], # 4번 CCTV: (상, 좌, 우), (하, 좌, 우), (상, 좌, 하), (상, 우, 하) 방향으로 갈 수 있음
        [[0, 1, 2, 3]] # 5번 CCTV: (상, 하, 좌, 우) 방향으로 갈 수 있음
]

# 감시방향을 확인해야하는 CCTV 모두 저장 (감시 방향을 확인할때마다 이중 for문을 도는건 비효율적임)
cctv_lst = []
for row in range(N):
        for col in range(M):
                cctv_mode = office[row][col]
                if 1<= cctv_mode <= 5:
                        cctv_lst.append((row, col, cctv_mode)) # cctv의 row, col, cctv번호 저장


min_area = float('inf') # 최소 사각지대 초기화
total_cctv = len(cctv_lst) # 전체 CCTV의 개수

# 감시할 수 있는 영역 확인
def can_monitor(array, dx ,dy, r, c): # 현재 office array, x방향, y방향, cctv의 row, cctv의 column
        nx, ny = r, c
        while True:
                nx, ny = nx + dx, ny + dy
                if not (0 <= nx < N and 0 <= ny < M) or array[nx][ny] == 6: # 인덱스 범위를 벗어나거나 벽이면
                        return
                
                if array[nx][ny] == 0:
                        array[nx][ny] = '#'


# 완전탐색 -> 갈 수 있는 모든 방향을 조합하면서 min_area를 업데이트
def dfs(current_cctv, array):
        global min_area

        # 종료조건: 모든 CCTV를 다 선택하면 종료
        if current_cctv == total_cctv:
                cnt = 0
                for r in range(N):
                        for c in range(M):
                                if array[r][c] == 0: cnt += 1
                
                min_area = min(min_area, cnt) # 최소 사각지대 개수 업데이트
                return 
        
        x, y, cctv_ver = cctv_lst[current_cctv] # cctv_lst의 current_cctv번째 CCTV 꺼내기

        # 이 cctv_mode가 갈 수 있는 방향의 모든 경우의 수 시도
        for direcitons in mode[cctv_ver]:
                # 맵 복사 (확정되기 전까지 맵을 훼손하면 안되니까)
                temp_arr = copy.deepcopy(array)

                # 선택된 방향으로 감시할 수 있는 영역 채우기
                for d in direcitons:
                        dx, dy = dir[d]
                        can_monitor(temp_arr, dx, dy, x, y) #현재 array, row 이동 방향, column 이동 방향, cctv의 row, cctv의 column

                dfs(current_cctv+1, temp_arr) # 다음 CCTV로 넘어가기



### 실행부 ###
dfs(0, office) # 선택한 CCTV 개수, 지금까지의 맵 array
print(min_area)