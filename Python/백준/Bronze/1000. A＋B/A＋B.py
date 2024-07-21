import sys
input = sys.stdin.readline
def add(x, y):
    return (x+y)
a, b = map(int, input().strip().split())
print(add(a, b))