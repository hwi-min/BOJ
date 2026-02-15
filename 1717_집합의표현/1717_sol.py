n, m = map(int, input().split())
parents = [i for i in range(n+1)]

# 해당 요소의 부모 찾기
def find_parent(elem):
    if parents[elem] != elem:  # 자기자신이 부모가 아니라면
        parents[elem] = find_parent(parents[elem])
        return parents[elem]
    return elem

# m개의 입력 받기
for _ in range(m):
    cmd, elem1, elem2 = map(int, input().strip().split())

    if cmd == 0: # 0: 합치기
        if find_parent(elem1) != find_parent(elem2): 
            parents[find_parent(elem2)] = elem1

    if cmd == 1: # 1: 같은 집합인지 확인하기
        if find_parent(elem1) == find_parent(elem2): # 부모가 동일하면
            print('YES')
        else:
            print('NO')

