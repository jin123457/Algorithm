import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0

for a, b, c in combinations(range(M), 3) :
    maxNm = 0
    for i in range(N) :
        maxNm += max(board[i][a],board[i][b],board[i][c])
    ans = max(ans,maxNm)

print(ans)