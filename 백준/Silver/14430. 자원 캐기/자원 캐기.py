import sys

input = sys.stdin.readline

N,M = map(int,input().split())
board = [[0] * (M + 1)]
for _ in range(N) :
    board.append([0] + list(map(int,input().split())))
DP = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1,N + 1) :
    for j in range(1,M + 1) :
        DP[i][j] = max(DP[i - 1][j],DP[i][j - 1]) + board[i][j]
print(DP[-1][-1])