import sys

input = sys.stdin.readline

def move_box(idx,A,N,M) :
    global ans
    for i in range(M) : 
        for j in range(N) :
            if A[j][i] :
                for k in range(j,N) :
                    if not A[k][i] :
                        ans[idx] += 1

def my_box(idx) :
    N,M = map(int,input().split())
    A = list()
    for _ in range(N) :
        A.append(list(map(int,input().split())))

    move_box(idx,A,N,M)

N = int(input())
ans = [0] * N
for i in range(N) :
    my_box(i)

print("\n".join(map(str,ans)))