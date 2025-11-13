n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def shift(row, dir):
    if dir == 'L':
        row.insert(0, row.pop())
    elif dir == 'R':
        row.append(row.pop(0))


# q초 만큼의 반복
for r, d in winds: # r: 영향을 받는 행 번호, d: 바람 불어오는 방향 >> O(q) : 최악 100
    r = r-1 # 인덱스 맞춰서 수정해주기

    if d == 'L': # 왼쪽에서 바람이 불어오면
        shift(a[r], "L")    

    elif d == 'R': # 오른쪽에서 바람이 불어오면
        shift(a[r], "R")

    direction = d # 초기 방향 설졍
    upper_flag = False
    lower_flag = False

    # 위쪽 전파 확인
    for upper_idx in range(r-1, -1, -1): # r부터 인덱스 0 row까지
        for col in range(m):
            if a[upper_idx+1][col] == a[upper_idx][col]: # 방향이 이미 바뀐 row와 요소가 같은 경우
                direction = "L" if direction == 'R' else 'R' # 방향을 역방향으로 바꾼 뒤
                shift(a[upper_idx], direction) # 역방향으로 수정
                upper_flag = True
                break # 일치하는 것이 없으면 그만 탐색
        
        else: break # for문이 break없이 모두 실행된 경우 해당 else문이 실행됨
    
    direction = d # 초기 방향 설졍

    # 아래쪽 전파 확인
    for lower_idx in range(r+1, n): # r 다음부터 마지막 row 인덱스까지
        for col in range(m):
            if a[lower_idx][col] == a[lower_idx-1][col]: # 요소가 같은 경우
                direction = 'L' if direction == 'R' else 'R'
                shift(a[lower_idx], direction)
                break # 일치하는 것이 없으면 그만 탐색
        else: break

for row in a:
    print(*row)