# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.



import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
parent_node = [0] * (n+1)

for _ in range(n-1):
    u, v = map(int, input().strip().split())
    tree[u].append(v)
    tree[v].append(u)

def bfs(start):
    queue = deque([start])
    parent_node[start] = -1  # 루트 노드의 부모를 -1로 설정 (루트 노드에는 부모가 없음)

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if parent_node[neighbor] == 0:  # 아직 부모가 설정되지 않은 경우
                parent_node[neighbor] = node
                queue.append(neighbor)

bfs(1)

for i in range(2, n+1):
    print(parent_node[i])
