# 문제
# 지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

# 문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

# 입력
# 지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

# 다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

# 출력
# 각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().strip().split())
matrix = [list(map(int, list(input().strip().split()))) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# x, y 는 2인 좌표
def bfs (x, y):
    queue = deque([(x, y)]) # deque에 (x, y)라는 하나의 튜플을 포함하여 초기화해야함
    distances = [[-1] * m for _ in range(n)]
    distances[x][y] = 0 # 시작 지점의 거리는 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and matrix[nx][ny]==1 and distances[nx][ny] == -1:
                queue.append((nx, ny))
                distances[nx][ny] = distances[x][y] + 1 # count 계산을 이런 방식으로 해야함
    
    return distances
                        

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            start_x, start_y = i, j
            break

distances = bfs(start_x, start_y)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(0, end=' ')
        else:
            print(distances[i][j], end=' ')
    print()