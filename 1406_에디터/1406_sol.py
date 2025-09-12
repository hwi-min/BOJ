"""
시간제한: 0.3초
문자열(N)의 최대길이: 100,000 (10만)
-> 중첩 for 안됩니다 !!! 
-> pointer 안됩니다 !!!
"""


strings = input()
M = int(input())
prev_stack, rear_stack = [], []

# 커서 기준 앞 부분에 차례대로 append
for l in strings:
    prev_stack.append(l)

# M만큼의 입력을 받으며 처리
for _ in range(M):
    inputs = input().split()
    if len(inputs) > 1:
        command, letter = inputs[0], inputs[1]
    command = inputs[0] # 길이가 1이면 command만 저장

    # 명렁어 처리
    if command == 'P':
        prev_stack.append(letter)
    elif command == 'L':
        if prev_stack:
            elem = prev_stack.pop()
            rear_stack.append(elem)

    elif command == 'D':
        if rear_stack:
            elem = rear_stack.pop()
            prev_stack.append(elem)
    elif command == 'B': 
        if prev_stack: prev_stack.pop()

print("".join(prev_stack)+"".join(reversed(rear_stack)))




