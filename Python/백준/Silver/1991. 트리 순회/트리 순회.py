# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

import sys
input = sys.stdin.readline

class BinaryTree:
    def __init__(self):
        self.tree = {}
        
    def add_node(self, root, left, right):
        self.tree[root] = (left, right)

    def preorder(self, node):
        if node == '.':
            return
        print(node, end ='')
        self.preorder(self.tree[node][0])
        self.preorder(self.tree[node][1])
        
    def inorder(self, node):
        if node == '.':
            return
        self.inorder(self.tree[node][0])   
        print(node, end='')
        self.inorder(self.tree[node][1])
        
    def postorder(self, node):
        if node == '.':
            return
        self.postorder(self.tree[node][0])
        self.postorder(self.tree[node][1])
        print(node, end='')
        
n = int(input())
bt=BinaryTree()

for _ in range(n):
    root, left, right = input().strip().split()
    bt.add_node(root, left, right)
    
bt.preorder('A')
print()
bt.inorder('A')
print()
bt.postorder('A')
print()

    