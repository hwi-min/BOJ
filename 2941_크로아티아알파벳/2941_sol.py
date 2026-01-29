"""
최대 100글자의 단어
"""

word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

# 1차로 길이가 가장 긴 알파벳을 한 글자로 치환
word = word.replace('dz=', '1')

# 나머지 치환
for cro in croatia:
    word = word.replace(cro, '2')

print(len(word))