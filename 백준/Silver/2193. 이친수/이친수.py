import sys

input = sys.stdin.readline

N = int(input())
A = [1,1]

for _ in range(N - 2) :
    A.append(A[-1] + A[-2])

print(A[-1])