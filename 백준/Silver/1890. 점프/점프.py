import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
DP[0][0] = 1
for i in range(N) :
    for j in range(N) :
        if i == N -1 and j == N - 1 :continue
        t = board[i][j]
        if j + t < N and DP[i][j] :
            DP[i][j + t] += DP[i][j]
        if i + t < N and DP[i][j] :
            DP[i + t][j] += DP[i][j]
print(DP[-1][-1])