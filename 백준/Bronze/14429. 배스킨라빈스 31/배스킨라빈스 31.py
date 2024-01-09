import sys

input = sys.stdin.readline

N = int(input())
obj = {}
for i in range(1,N + 1) :
    J,M = map(int,input().split())
    J -= 1
    M += 1
    R = J % M
    total = 0
    for _ in range(R,J + 1,M) :
        total += 1
    obj[i] = total * 2

print(*sorted(obj.items(),key=lambda x:x[1])[0])