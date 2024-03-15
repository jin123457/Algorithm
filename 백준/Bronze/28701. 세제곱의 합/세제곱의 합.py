import sys

input = sys.stdin.readline

N = int(input())
T = 0
Tr = 0
for i in range(1,N + 1):
    T += i
    Tr += (i ** 3)
print(T)
print(T ** 2)
print(Tr)