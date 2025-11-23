n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
total = 0 # 최종 개수 초기화

# 행복한 수열인지 확인하는 함수 정의
def checking(elems, n, m):
    if m == 1: # m == 1인 경우에는 모든 행과 열이 행복한 수열이므로
        return True

    # 이외의 경우
    current_status = 1 

    for i in range(1, n):
        if elems[i] == elems[i-1]: # 앞의 요소와 동일한 경우
            current_status += 1 # 1 증가
        else: # 다른 경우
            current_status = 1 # 연속하지 않으므로 current_status를 1로 다시 초기화

        if current_status >= m: # 만약 current_status가 m과 같거나 크면
            return True # 행복한 수열이라고 판단
            
    return False # 이외의 경우 False 반환

for r in range(n):
    rows = grid[r] # 행 리스트
    if checking(rows, n, m): # checking이 True(행복한 수열)이면
        total += 1 # 최종 개수 += 1

for c in range(n):
    cols = [] # 열 리스트 초기화
    for r in range(n): # for문을 돌면서 열 리스트 생성
        cols.append(grid[r][c])

    if checking(cols, n, m): # checking이 True(행복한 수열)이면
        total += 1 # 최종 개수 += 1

print(total)
