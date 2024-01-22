import sys

input = sys.stdin.readline

N = int(input())
A = [0,1,2]

for _ in range(N - 2) :
    A.append((A[-1] + A[-2]) % 10007)
print(A[N])