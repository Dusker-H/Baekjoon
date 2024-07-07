# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 
# 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 
# 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

import sys
from collections import deque
input=sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

queue=deque([]) # deque 생성

dx, dy = [1,-1,0,0],[0,0,1,-1] # dx[0], dy[0] = (1, 0), dx[3],dy[3] = (0, 1)
result = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j]==1:
            queue.append([i, j])

def bfs():
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if(0<=nx<N and 0<=ny<M and matrix[nx][ny]==0):
                matrix[nx][ny]=1+matrix[x][y]
                queue.append([nx, ny])
                          
bfs()

# 익지 않은 토마토가 있는지 확인 및 최대 일수 계산
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, matrix[i][j])

# 시작일을 1로 표현했으니 1을 빼줌
print(result - 1)