from collections import deque

N, M = map(int, input().split()) # 퍼즐 꾸러미개수 N, 꾸러미속 퍼즐 개수 M
puzzles = [set(map(int, input().split())) for _ in range(N)] 

target = set(range(10)) # 목표: 0~9까지 다 모은 상태
queue = deque([(set(), 0)]) # (현재까지 모은 숫자들, 사용한 꾸러미 개수)
visited = [frozenset()]

# bfs
while queue:
    # 현재까지 모은 퍼즐, 현재까지 사용한 꾸러미 개수
    current_set, cnt = queue.popleft()

    # target과 동일한 set을 찾으면 cnt 출력
    if current_set == target:
        print(cnt)
        break

    for puzzle in puzzles:
        next_set = current_set | puzzle # 두 set의 합집합
        frozen_next = frozenset(next_set) # 이미 왔던 길이라는 것을 알려주기 위한 visitied

        if frozen_next not in visited: # 이미 왔던 길이 아니라면
            visited.append(frozen_next) # visited에 추가하고
            queue.append((next_set, cnt+1)) # 현재까지 모은 퍼즐, 꾸러미 개수 + 1 