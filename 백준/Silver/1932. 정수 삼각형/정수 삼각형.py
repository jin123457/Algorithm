import sys

input = sys.stdin.readline

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
dp = [[] for _ in range(N)]
dp[0] = A[0]

for i in range(1,N) :
    for j in range(len(A[i])) :
        if j == 0 :
            dp[i].append(A[i][j] + dp[i - 1][j])
        elif j == len(A[i]) - 1:
            dp[i].append(A[i][j] + dp[i - 1][j - 1])
        else :
            dp[i].append(max(A[i][j] + dp[i - 1][j - 1],A[i][j] + dp[i - 1][j]))  
print(max(dp[N - 1]))