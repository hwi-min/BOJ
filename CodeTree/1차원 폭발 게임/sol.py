"""
시간 제한: 1초 -> 1억
1 <= N, M <= 100

결과물
- 최종적으로 남은 폭탄의 개수
- 위에서 아래 방향으로 남은 폭탄의 숫자
"""

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)] # 폭탄의 순서는 위에서 -> 아래로

while True:
    if not numbers:
        break

    is_exploded = False # 이번 턴에서 폭발이 일어났는지 체크
    temp_result = [] # 임시 결과물 저장

    now_num = numbers[0]
    cnt = 1
    is_find = True if cnt >= m else False

    for i in range(1, len(numbers)):
        if numbers[i] == now_num: # 지금 비교하는 숫자와 같고 아직 m개 연속을 못 찾았다면
            cnt += 1
            if not is_find and cnt >= m: # m보다 같거나 크고 처음 m을 넘었다면 
                is_find = True # Flag를 True로 변경
        
        elif not is_find and numbers[i] != now_num: # 아직 비교하는 숫자가 m개 연속이 안나왔는데 새로운 요소가 등장했다면
            temp_result.extend([now_num] * cnt) # 비교 끝난 숫자는 넣어줌
            now_num = numbers[i] # 비교군 숫자를 바꿔주고
            cnt = 1 # cnt는 1로 다시 초기화
            is_find = True if cnt >= m else False # 히캐 해결을 위한 코드 수정 부분 
            
        elif is_find and numbers[i] != now_num: # 비교하는 숫자가 m개 연속이 나왔고, 다른 숫자가 등장했으면
            is_exploded = True
            now_num = numbers[i]
            cnt = 1
            is_find = True if cnt >= m else False # flag도 다시 False로 바꿔주기

            # append는 해줄필요 없음!

            # now_num = numbers[i]
            # is_find = True if cnt >= m else False

    if not is_find: # 아직 m개를 넘지 않았다면
        temp_result.extend([now_num] * cnt)
    else: # m개를 넘었다면
        is_exploded = True # 이번 턴에 터졌다고 알려주기

    numbers = temp_result # 업데이트 된 리스트로 초기화

    if not is_exploded:
        break # 이번 반복문에서 한 번도 폭발이 없었으면 시뮬레이션 종료

print(len(numbers))

for elem in numbers:
    print(elem)