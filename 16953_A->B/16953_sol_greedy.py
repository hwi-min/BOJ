A, B = map(int, input().split())
cnt = 1

# greedy
while True:

    if A == B:
        print(cnt)
        break
    
    if (A > B) or ((B % 10 != 1) and (B % 2 != 0)):
        print(-1)
        break

    if B % 10 == 1:
        B //= 10
        cnt += 1

    elif B % 2 == 0:
        B //= 2
        cnt += 1