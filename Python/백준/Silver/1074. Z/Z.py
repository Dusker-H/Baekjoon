import sys
input = sys.stdin.readline

N, r, c = map(int, input().strip().split())

def z_order(n, x, y):
    if n==0:
        return 0
    half = 2**(n-1)
    if x < half and y < half:
        return z_order(n-1, x, y)
    elif x < half and y >= half:
        return half * half + z_order(n-1, x, y-half)
    elif x >= half and y < half:
        return 2*half*half + z_order(n-1, x-half, y)
    else:
        return 3*half*half + z_order(n-1, x-half, y-half)
    
print(z_order(N, r, c))