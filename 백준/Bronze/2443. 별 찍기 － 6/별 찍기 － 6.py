import sys

input = sys.stdin.readline

N = int(input())
target = N * 2 - 1
for i in range(N + 1) :
    print(' ' * i,end="")
    print('*' * target)
    target -= 2