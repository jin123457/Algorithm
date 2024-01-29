import sys

input = sys.stdin.readline

N = int(input())
target = 1
for i in range(N - 1,-1,-1) :
    print(' ' * i,end="")
    print('*' * target)
    target += 2