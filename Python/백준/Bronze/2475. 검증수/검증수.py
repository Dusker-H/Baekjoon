import sys
input = sys.stdin.readline

arr = list(map(int, input().strip().split()))
sum=0
for i in range(5):
    sum+=arr[i]**2%10
    
print(sum%10)