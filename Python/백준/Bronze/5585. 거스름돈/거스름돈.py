
import sys
input = sys.stdin.readline

n = int(input())
n = 1000-n
count = 0
arr = [500, 100, 50, 10, 5, 1]

for coin in arr:
    count += n//coin
    n %=coin
    
print(count)