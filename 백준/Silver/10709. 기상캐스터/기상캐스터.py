import sys

input = sys.stdin.readline

N,M = map(int,input().split())
A = list(list(map(str,input().rstrip())) for _ in range(N))

for i in range(len(A)) :
    wh = list()
    for j in range(len(A[i])) :
        if A[i][j] == "c" :
            A[i][j] = 0
            wh.append((i,j))
        else :
            if len(wh) == 0 :
                A[i][j] = -1
            else :
                A[i][j] = j - wh[-1][1]

for a in A :
    print(*a)