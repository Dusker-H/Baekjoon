import sys
input=sys.stdin.readline

def count(n):
    
    dp=[[] for _ in range(41)]
    dp[0]=[1, 0]
    dp[1]=[0, 1]
    if n==0:
        return dp[0]
    elif n==1:
        return dp[1]
    elif n>1:
        for i in range(2, n+1):
            dp[i]=[dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]
            
        return dp[n]


t=int(input())

n=[int(input().strip()) for _ in range(t)]
results=[]

for i in range(t):
    results.append(count(n[i]))
    
for result in results:
    print('{} {}'.format(result[0], result[1]))

