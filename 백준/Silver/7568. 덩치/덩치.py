import sys

input = sys.stdin.readline

N = int(input())
A = list(list(map(int,input().split())) for _ in range(N))
ans = [1] * N

for i in range(len(A)) :
    for j in range(len(A)) :
        if i == j : continue
        if A[i][0] < A[j][0] and A[i][1] < A[j][1] :
            ans[i] += 1

print(*ans)