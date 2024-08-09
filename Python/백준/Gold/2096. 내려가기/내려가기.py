import sys
input = sys.stdin.readline

N = int(input().strip())

# 첫 줄 입력 처리
prev_max = list(map(int, input().strip().split()))
prev_min = prev_max[:]

for _ in range(1, N):
    scores = list(map(int, input().strip().split()))
    
    # 현재 줄의 최대값을 저장할 리스트
    curr_max = [0] * 3
    curr_min = [0] * 3

    # 현재 줄의 최대값 계산
    curr_max[0] = max(prev_max[0], prev_max[1]) + scores[0]
    curr_max[1] = max(prev_max[0], prev_max[1], prev_max[2]) + scores[1]
    curr_max[2] = max(prev_max[1], prev_max[2]) + scores[2]

    # 현재 줄의 최소값 계산
    curr_min[0] = min(prev_min[0], prev_min[1]) + scores[0]
    curr_min[1] = min(prev_min[0], prev_min[1], prev_min[2]) + scores[1]
    curr_min[2] = min(prev_min[1], prev_min[2]) + scores[2]

    # 다음 반복을 위해 현재 줄의 결과를 이전 값으로 업데이트
    prev_max = curr_max
    prev_min = curr_min

# 결과 출력
print(max(prev_max), min(prev_min))
