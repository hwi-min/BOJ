K = int(input()) # K는 최대 100,000(10만)
stack = []

for _ in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    else: stack.pop()

print(sum(stack))