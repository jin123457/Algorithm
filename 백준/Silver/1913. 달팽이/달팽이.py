import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
A = [deque() for _ in range(N)]
S = N // 2
dirflag = ["up","right","down","left"]
nm = 0
A[S].append(1)
repeat = 2
repeat_nm = 1
repeat_nm1 = 1
coordinates = []
for i in range(2,N * N + 1) :
    repeat_nm1 -= 1
    if repeat_nm1 <= 0 :
        repeat -= 1
    if dirflag[nm] == "up" :
        S -= 1
        A[S].appendleft(i)

    elif dirflag[nm] == "right" :
        A[S].append(i)

    elif dirflag[nm] == "down" :
        S += 1
        A[S].append(i)
    elif dirflag[nm] == "left" :
        A[S].appendleft(i)
        
    if repeat_nm1 <= 0 :
        if repeat <= 0 :
            repeat = 2
            repeat_nm += 1
        repeat_nm1 = repeat_nm
        nm = (nm + 1) % 4

for i in range(N) :
    ans = []
    for j in range(N) :
        ans.append(A[i][j])
        if A[i][j] == M :
            coordinates.append(i + 1)
            coordinates.append(j + 1)
    
    print(*ans)

print(*coordinates)