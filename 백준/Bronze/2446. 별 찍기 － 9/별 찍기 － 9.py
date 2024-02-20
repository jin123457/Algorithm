import sys

input = sys.stdin.readline

N = int(input())

for i in range(N * 2 - 1,-1, -2) :
  print(' ' * ((N * 2 - 1 - i) // 2),end="")
  print('*' * i)
for i in range(3,N * 2,2) :
  print(' ' * ((N * 2 - i) // 2),end="")
  print('*' * i)