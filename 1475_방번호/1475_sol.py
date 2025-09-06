"""
시간 제한 -> 2초 (2억)
다솜이의 방 번호 N은 최대 10,000,000 (백만) -> for문 1회로 정리해야 함
"""
 

### sol_1 (시간복잡도: O(N))
room_num = input() # str 형태로 받아오기
num_dict = {i:1 for i in range(10)} # 0부터 9까지 사용할 수 있는 개수가 처음엔 1개씩이므로 1로 초기화
cnt = 1

for elem in room_num: # 각 숫자를 돌면서 (단, 이때 숫자는 str) -> O(N)
    elem = int(elem) # 정수로 형변환
    if num_dict[elem] > 0: # 해당 숫자가 사용할 수 있는 횟수가 0보다 크다면?
        num_dict[elem] -= 1 # 사용 횟수를 1회 감소시킨다
    elif num_dict[elem] == 0 and (elem == 6 or elem == 9): # 사용 횟수가 안남았는데, 이때 6이거나 9이면 확인 필요
        # elem이 6인데, 9의 사용횟수가 남았다면? -> 9를 1 감소
        if elem == 6 and num_dict[9] > 0: num_dict[9] -= 1
        # elem이 9인데, 6의 사용횟수가 남았다면? -> 6를 1 감소
        elif elem == 9 and num_dict[6] > 0: num_dict[6] -= 1
        else: # 둘 다 이미 사용했다면?
            cnt += 1
            for key in num_dict: # -> O(10)
                if key != elem: num_dict[key] += 1 # elem은 바로 사용할거니까, 그것 제외 모든 숫자의 사용 횟수를 1개씩 올림
    else: # 그 외의 경우 (사용할 수 있는 횟수가 남지 않고 6이나 9가 아닌 경우)
        cnt += 1 # 갱신과 동시에 -> 사용 !
        for key in num_dict:
            if key != elem: num_dict[key] += 1
print(cnt)   


### sol_2 (시간복잡도: O(N) 단, 공간복잡도가 훨씬 나음)
room_num = input() # str 형태로 받아오기
num_dict = {i:0 for i in range(10)} # 0부터 9까지 사용할 수 있는 개수가 처음엔 1개씩이므로 1로 초기화

# 전체 방 숫자를 돌면서
for elem in room_num:
    num_dict[int(elem)] += 1 # 사용 개수 1개씩 증가

six_nine = (num_dict[6] + num_dict[9]) // 2 # 6과 9는 결국 같은 숫자니까! 사용 개수 나누기 2
num_dict[6], num_dict[9] = six_nine, 0 # 6만 사용하고 9는 사용하지 않겠다!

print(max(list(num_dict.values()))) # 전체 values 중 가장 큰 값이 최소 필요한 숫자세트의 수

