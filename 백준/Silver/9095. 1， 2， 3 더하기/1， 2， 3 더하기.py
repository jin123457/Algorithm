import sys

input = sys.stdin.readline

A = [1,2,4]
for _ in range(7) :
    A.append(A[-1] + A[-2] + A[-3])
T = int(input())

for _ in range(T) :
    N = int(input())
    print(A[N - 1])