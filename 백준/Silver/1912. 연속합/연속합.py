import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
ans = [0] * N
ans[0] = A[0]
for i in range(1,len(A)) :

    if ans[i - 1] + A[i] > A[i] :
        ans[i] = ans[i - 1] + A[i]
    else :
        ans[i] = A[i]
    
print(max(ans))