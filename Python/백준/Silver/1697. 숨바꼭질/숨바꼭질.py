# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
# 5 17 = 4 수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
# 5-4-8-16-17

import sys
input=sys.stdin.readline
from collections import deque

def find_sister(n, k):
    max=100000
    visited=[False]*(max+1)
    
    # BFS를 위한 큐를 초기화합니다. (현재 위치, 시간)
    queue=deque([(n, 0)])
    visited[n]=True
    
    while queue:
        current_pos, time = queue.popleft()
        

        if current_pos==k:
            return time
        
        next_positions=[current_pos+1, current_pos-1, current_pos*2]
        
        for next_pos in next_positions:
            if (0 <= next_pos <= max and not visited[next_pos]):
                queue.append((next_pos, time+1))
                visited[next_pos]=True
                

n, k = map(int, input().split())
print(find_sister(n,k))