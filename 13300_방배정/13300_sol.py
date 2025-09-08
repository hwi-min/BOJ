"""
학생수(N)이 최대 1000
한 방 최대 인원 수(K)가 최대 1000

같은 학년, 같은 성별로만 방을 구성할 수 있음 !
"""
N, K = map(int, input().split())  # 학생 수, 한 방의 최대 인원 수
stu_dict = {i: [0, 0] for i in range(1, 7)}  # 학생 정보 dict 초기화
cnt = 0

for _ in range(N):
    s, y = map(int, input().split())  # 성별, 학년 (여학생0, 남학생1)
    stu_dict[y][s] += 1

for key, value in stu_dict.items():
    for s in value:
        if s > 0:
            # 올림을 적용하여 필요한 방의 개수 계산
            cnt += (s + K - 1) // K

print(cnt)