"""
시간 제한: 1초 -> 1억
1 <= N, M <= 100

결과물
- 최종적으로 남은 폭탄의 개수
- 위에서 아래 방향으로 남은 폭탄의 숫자
"""

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)] # 폭탄의 순서는 위에서 -> 아래로
now_num = numbers[0]
cnt = 1
result = []
is_find = False

for i in range(1, n):
    if numbers[i] == now_num: # 지금 비교하는 숫자와 같고 아직 m개 연속을 못 찾았다면
        cnt += 1
        if not is_find and cnt >= m: # m보다 같거나 크고 처음 m을 넘었다면 
            is_find = True # Flag를 True로 변경
     
    elif not is_find and numbers[i] != now_num: # 아직 비교하는 숫자가 m개 연속이 안나왔는데 새로운 요소가 등장했다면
        result.append(now_num) # 비교 끝난 숫자는 넣어줌
        now_num = numbers[i] # 비교군 숫자를 바꿔주고
        cnt = 1 # cnt는 1로 다시 초기화
        
    elif is_find and numbers[i] != now_num: # 비교하는 숫자가 m개 연속이 나왔고, 다른 숫자가 등장했으면
        now_num = numbers[i]
        cnt = 1
        is_find = False # flag도 다시 False로 바꿔주기

        # append는 해줄필요 없음!
        
    

