
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
input=sys.stdin.readline
from collections import deque

def bfs(matrix, v, visited):
    queue=deque([])
    visited[v]=True
    queue.append(v)
    while queue:
        i = queue.popleft()
        for j in range(n):
            if matrix[i][j]==1 and not visited[j]:
                queue.append(j)
                visited[j]=True
        
        
def count_conneted_components(matrix, n):
    visited=[False]*n
    count=0
    for i in range(n):
        if not visited[i]:
            bfs(matrix, i, visited)
            count+=1
            
    return count
    

n, m = map(int, input().split())

matrix = [[0]*n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x-1][y-1]=1
    matrix[y-1][x-1]=1
    
print(count_conneted_components(matrix, n))