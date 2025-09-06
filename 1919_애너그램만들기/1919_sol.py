
"""
한 단어의 길이가 최대 1000자, 시간제한이 2초 (2억)이므로
for문 한 번 돌면? 1000
    두 번 돌면? 1000000 (백만) ------------------- > 최대 for문은 2번만 가능 
    세 번 돌면? 10000000000 (백억) -> 안됨

- 결국 공동으로 존재하는 단어들의 개수는 제외하고 나머지는 다 삭제하면 되니까 ..
"""

# input 받기
str1 = input()
str2 = input()

# 딕셔너리 초기화
str_dict = {}

cnt = 0

# str1을 돌면서 str_dict에 문자 개수 넣기
for letter in str1:
    if letter not in str_dict.keys():
        str_dict[letter] = 0

    str_dict[letter] += 1


# str2 돌면서 더합시당
for letter in str2:
    if letter in str_dict.keys():
        if str_dict[letter] > 0:
            str_dict[letter] -= 1
        else: # 0 이하이면 어쨌든 삭제해야하니까
            cnt += 1

    else: # 없으면
        cnt += 1

for key, value in str_dict.items():
    if value != 0:
        cnt += value

##################################################################################
# sum(list(str_dict.values()))과 위의 for문 중 어떤 것이 더 효율적인가?
# - > 시간 복잡도는 모두 O(N)으로 동일 / 리스트를 복사하기 때문에
# - > 하지만, list(str_dict.values())는 새로운 리스트 생성하므로 추가적 메모리가 더 들 수 있음
# print(cnt + sum(list(str_dict.values())))
##################################################################################

print(cnt)