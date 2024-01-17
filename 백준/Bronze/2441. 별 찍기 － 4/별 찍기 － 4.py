import sys

input = sys.stdin.readline

N = int(input())
A = [['*'] * N for _ in range(N)]

for i in range(N) :
    if i == 0 : continue
    else :
        for j in range(0,i) :
            A[i][j] = ' '
for i in range(len(A)) :
    print("".join(A[i]))