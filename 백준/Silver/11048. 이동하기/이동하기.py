import sys

input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
DP = [[0] * M for _ in range(N)]
DP[0][0] = board[0][0]
for i in range(N) :
    for j in range(M) :
        if i + 1 < N :
            DP[i + 1][j] = max(DP[i + 1][j],DP[i][j] + board[i + 1][j])
        if j + 1 < M :
            DP[i][j + 1] = max(DP[i][j + 1],DP[i][j] + board[i][j + 1])
        if i + 1 < N and  j + 1 < M :
            DP[i + 1][j + 1] = max(DP[i + 1][j + 1],DP[i][j] + board[i + 1][j + 1])

print(DP[N - 1][M - 1])