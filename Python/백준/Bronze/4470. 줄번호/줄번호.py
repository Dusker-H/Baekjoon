import sys
input = sys.stdin.readline

n = int(input())
sentences=[]
for i in range(n):
    sentences.append(input())

for i in range(n):
    print("{}. {}".format(i+1,sentences[i]),end='')
    