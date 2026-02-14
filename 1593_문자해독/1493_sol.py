# G: 1<= G <= 3000
# S: G <= S <= 3,000,000
# 순열쓰면 터진다

G, S = map(int, input().split()) # g: W의 길이 / s: 벽화에서 추출한 문자열 길이
w = input()
s = input()
w_count = [0] * 52 # 소문자 26개, 대문자 26개
s_count = [0] * 52 # 소문자 26개, 대문자 26개
cnt = 0

# 알파벳을 정수로 바꾸는 함수 정의
def char_to_ord(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') # a가 0, b가 1 .. 로 세팅
    else: # 대문자인경우
        return ord(char) - ord('A') + 26 # 마찬가지로 A가 0, B가 1인데 대소문자 구분해야하므로 26 더해서 정의

# 초기 세팅
for i in range(G):
    w_letter = w[i] # i번째 알파벳 추출
    w_count[char_to_ord(w[i])] += 1 # 존재한다고 체크
    s_count[char_to_ord(s[i])] += 1 # 존재한다고 체크

# 초기 세팅 값이 둘이 동일하면 cnt 세기
if w_count == s_count:
    cnt += 1

# 남은 문자열 슬라이딩 윈도우로 처리
for i in range(G, S): # G번째 인덱스부터 S길이 이내 인덱스까지
    s_count[char_to_ord(s[i-G])] -= 1 # 앞에 문자열 빼고
    s_count[char_to_ord(s[i])] += 1 # 뒤에 문자열 넣고

    # 동일하면 cnt 세기
    if w_count == s_count:
        cnt += 1 

print(cnt)