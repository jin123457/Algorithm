import sys

input = sys.stdin.readline

N = int(input())
board = [[0] * 3 for _ in range(3)]

for _ in range(9) :
  x,y = map(int,input().split())
  board[x - 1][y - 1] = N

  if board[x - 1] == [N] * 3 :
    print(N)
    exit()
  elif board[0][y - 1] == board[1][y - 1] == board[2][y - 1] == N :
    print(N)
    exit()
  elif board[0][0] == board[1][1] == board[2][2] == N or board[0][2] == board[1][1] == board[2][0] == N:
    print(N)
    exit()
  
  N = 1 if N == 2 else 2

print(0)