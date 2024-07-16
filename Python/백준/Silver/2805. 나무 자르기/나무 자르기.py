
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())

trees=list(map(int, input().strip().split()))

# 나무의 수가 N과 일치하는지 확인합니다.
if len(trees) != n:
    raise ValueError("입력된 나무의 수가 주어진 N과 일치하지 않습니다.")

start, end = 0, max(trees)

def get_wood_amout(height):
    return sum(tree - height if tree>height else 0 for tree in trees)
    
result=0

# 이진탐색을 통한 최대값 계산
while start <= end:
    mid=(start+end)//2
    wood = get_wood_amout(mid)
    
    if wood>=m:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)