# 계단 오르는 데는 다음과 같은 규칙이 있다.

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
#<----->
# 단계별 접근 방식

# 점화식 정의:
# dp[i]를 i번째 계단까지의 최대 점수라고 정의합니다.
# i번째 계단을 밟는 경우는 두 가지로 나눌 수 있습니다:
# i-1번째 계단을 밟고 i번째 계단을 밟는 경우 (i-2번째 계단을 밟지 않음)
# i-2번째 계단을 밟고 i번째 계단을 밟는 경우

# 점화식:
# dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
# 여기서 stairs[i]는 i번째 계단의 점수입니다.

# 기저 조건 설정:
# dp[0] = stairs[0]
# dp[1] = stairs[0] + stairs[1]
# dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

import sys
input = sys.stdin.readline

def max_score_stairs(stairs):
    
    n=len(stairs)
    
    if n==0:
        return 0
    elif n==1:
        return stairs[0]
    elif n==2:
        return stairs[0]+stairs[1]

    dp=[0]*n
    dp[0]=stairs[0]
    dp[1]=stairs[0]+stairs[1]
    dp[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])
    
    for i in range(3, n):
        dp[i]=max(stairs[i]+dp[i-2],stairs[i]+stairs[i-1]+dp[i-3])
        
        
    return dp[-1]

def main():
    
    n=int(input())
    
    # stairs=[0]*n
    # for i in range(n):
    #     stairs[i]=int(input())
    
    stairs = [int(input()) for _ in range(n)]
    print(max_score_stairs(stairs))
    
if __name__ == "__main__":
    main()