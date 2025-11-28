# dfs -> 경우의 수는 무조건 1개 밖에 없으니까 굳이 모든 경우를 다 가 볼 필요가 없음
A, B = map(int, input().split())
result = -1

def dfs(current_num, current_cnt):
    global result

    if current_num == B:
        result = current_cnt
        return
    
    if current_num > B:
        return
    
    dfs(current_num * 2, current_cnt+1)
    dfs(current_num * 10 + 1, current_cnt+1)

dfs(A, 1) # 현재, cnt
print(result)
