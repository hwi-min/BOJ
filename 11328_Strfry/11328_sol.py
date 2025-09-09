"""
dict에 첫 알파벳을 돌면서 개수 저장
두번째 str을 돌면서 -
"""
N = int(input())
for _ in range(N):
    letter_dict = {}
    str1, str2 = input().split()
    if len(str1) != len(str2):
        print('Impossible')
        continue

    for s in str1:
        if s not in letter_dict.keys():
            letter_dict[s] = 1
        else: letter_dict[s] += 1

    possible = True

    for s in str2:
        if s not in letter_dict.keys() or letter_dict[s] == 0:
            possible = False
            break
        letter_dict[s] -= 1

    print('Possible' if sum(letter_dict.values()) == 0 else 'Impossible')

