import sys
input = sys.stdin.readline

# 민국이의 점수 입력
minguk_scores = list(map(int, input().strip().split()))
# 만세의 점수 입력
manse_scores = list(map(int, input().strip().split()))

# 총점 계산
S = sum(minguk_scores)
T = sum(manse_scores)

# 결과 출력
print(max(S, T))
