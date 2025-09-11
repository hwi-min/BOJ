"""
시간제한: 1,000,000 (백만) -> 중첩 for문 사용 불가
스택 시간 복잡도
- append, pop: O(N)

* 문제 풀이 방식
- 2개의 스택 사용
- 커서를 중심으로 커서 왼쪽 스택과 뒤 스택으로 나누어 pop, push로 연산
"""

N = int(input())
commands = ('-', '<', '>')
# 커서 기준 앞 뒤를 나누어서 스택 만들기

for _ in range(N):
    prev_stack, rear_stack = [], []
    inputs = input()

    for cm in inputs: # 전체 inputs를 돌면서 확인
        if cm not in commands: # 만약 commands에 해당되지 않는다면 커서 앞에 삽입
            prev_stack.append(cm)
        # commands에 해당되는 입력이 들어왔다면 ...
        else:
            # 왼쪽으로 한칸이동 명령이 들어왔다면...
            if cm == '<': 
                if prev_stack:# 앞에 스택이 존재한다면 -> 앞 스택에서 pop -> 뒤 스택에 push
                    elem = prev_stack.pop()
                    rear_stack.append(elem)
                # else: 앞에 스택이 이미 아무것도 없다면? -> 건들 필요 없음 !
            elif cm == '>':
                if rear_stack: # 뒤의 스택이 존재한다면 -> 뒤 스택에서 pop -> 앞 스택에 push
                    elem = rear_stack.pop()
                    prev_stack.append(elem)
                # else: 뒤 스택이 이미 아무것도 없다면 -> 건들 필요 없음
            elif cm == '-':
                if prev_stack:
                    elem = prev_stack.pop()

    print("".join(prev_stack) + "".join(reversed(rear_stack)))
