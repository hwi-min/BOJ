from collections import deque

N = int(input())
cards = deque(range(1, N+1))
cnt = N
pop_flag = True

while cnt > 1:
    if pop_flag: # pop만 할 차례인 경우
        cards.popleft() # 가장 위에 요소 삭제
        pop_flag = False 
        cnt -= 1

    else:
        cards.rotate(-1)
        pop_flag = True

print(cards[0])
