import sys

input = sys.stdin.readline

A1,A0 = map(int,input().split())
C = int(input())
N0 = int(input())

if A1 * N0 + A0 <= N0 * C and A1 <= C:
    print(1)
else :
    print(0)