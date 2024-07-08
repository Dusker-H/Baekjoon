import sys
input = sys.stdin.readline

from collections import deque

# 좌표를 위한 방향리스트 설정
dx, dy = [1,-1,0,0],[0,0,1,-1] # dx[0], dy[0] = (1, 0), dx[3],dy[3] = (0, 1)

def bfs(x, y):
    queue=deque([])
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if (0<=nx<m and 0<=ny<n and matrix[nx][ny]==1):
                matrix[nx][ny]=0
                queue.append([nx, ny])


t = int(input())
results=[]
for _ in range (t):
    m, n, k = map(int, input().split())
    matrix = [[0]*n for _ in range(m)]
    count=0
    
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y]=1
        
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1:
                bfs(i, j)
                count +=1 
    
    results.append(count)
    
for result in results:
    print(result)