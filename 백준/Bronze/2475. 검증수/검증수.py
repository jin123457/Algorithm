import sys

input = sys.stdin.readline

A = list(map(int,input().split()))
total = 0
for a in A :
    total += a ** 2
print(total % 10)