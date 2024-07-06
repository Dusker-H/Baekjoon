import sys

input=sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self, x):
        self.queue.append(x)
        
    def dequeue(self):
        if self.empty():
            return -1
        else:
            return self.queue.pop(0)
        
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return 1 if len(self.queue)==0 else 0
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[0]
        
    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[-1]
        
class Graph:
    def __init__(self):
        self.graph={}
        
    def insert_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
        
    def insert_node(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)
    
    def sort_adjacency_list(self):
        for key in self.graph:
            self.graph[key].sort()

        

def dfs_recursive(graph, v):
    #방문 결과를 담을 리스트와 방문 여부를 확인할 집합을 만든다.
    res = []
    visited = set()

    #깊이 우선 탐색하는 재귀함수를 만든다.
    def _dfs(u):
        # 이미 방문한 노드이면 종료한다.
        if u in visited:
            return

        #현재 노드를 방문 처리한다.
        #즉, 방문 결과 리스트와 방문 여부를 확인할 집합에 추가한다.
        visited.add(u)
        res.append(u)

        #현재 노드와 간선으로 연결된 노드들을 깊이 우선 탐색한다.
        for v in graph.graph[u]:
            _dfs(v)

    _dfs(v)
    return res

def bfs_recursive(graph, v):
    res =[]
    visited = set()
    visited.add(v)
    queue=Queue()
    queue.enqueue(v)
    
    while queue.size()>0:
        u = queue.dequeue()
        res.append(u)
        for w in graph.graph[u]:
            if w not in visited:
                visited.add(w)
                queue.enqueue(w)
    return res

    
def main():
    graph=Graph()
    N, M, V = map(int, input().split()) # map 함수 활용
    
    for i in range(1, N+1): # 정수 입력!
        graph.insert_vertex(i)
        
    commands=[input().strip() for _ in range(M)]
    
    for command in commands:
        v, w = map(int, command.split())
        graph.insert_node(v, w)
    
    graph.sort_adjacency_list()
    dfs_results=dfs_recursive(graph, V)
    bfs_results=bfs_recursive(graph, V)
    
    for dfs_result in dfs_results:
        print(dfs_result, end=' ')
    print()
    
    for bfs_result in bfs_results:
        print(bfs_result, end=' ')
    print()
    
if __name__=="__main__":
    main()