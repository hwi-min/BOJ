"""
시간제한 -> 1초 (1억 10**8)
n은 최대 100,000(10만) -> for문 1회 내로 완료해야함
x는 최대 2,000,000(100만)
"""

n = int(input()) # 수열의 개수
sequences = list(map(int, input().split()))
x = int(input()) # 만들고자하는 수

sequences.sort() # sequence 정렬 (오름차순) ->< O(n log n)
# 투 포인터 초기화
left, right = 0, n-1

cnt = 0

while left < right: # 두 포인터가 만나기 전까지 반복 -> O(N)
    current_sum = sequences[left] + sequences[right]
    if current_sum == x: 
        cnt += 1 # 두 합이 x라면 cnt 증가
        # 쌍을 찾았으니 left, right도 조정
        left, right = left+1, right-1
    elif current_sum < x: # 목표값보다 현재 합이 작다? -> 더 큰 값이 필요
        left += 1
    elif current_sum > x: # 목표값보다 현재 합이 크다? -> 더 작은 값이 필요
        right -= 1

print(cnt)
        