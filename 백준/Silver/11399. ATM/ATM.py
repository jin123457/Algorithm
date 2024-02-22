import sys

input = sys.stdin.readline

N = int(input())
P = sorted(map(int,input().split()))
ATM = [0] * N
ATM[0] = min(P)

for i in range(1,len(P)) :
    ATM[i] = ATM[i - 1] + P[i]

print(sum(ATM))