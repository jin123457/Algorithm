import sys

input = sys.stdin.readline

M = int(input())
cups = [[] for _ in range(3)]
cups[0] = [1]
for _ in range(M) :
    X,Y = map(int,input().split())

    if X == Y : continue

    if (X == 1 and Y == 2) or (X == 2 and Y == 1) :
        cups[0],cups[1] = cups[1],cups[0]
    
    if (X == 1 and Y == 3) or (X == 3 and Y == 1) :
        cups[0],cups[2] = cups[2],cups[0]

    if (X == 2 and Y == 3) or (X == 3 and Y == 2) :
        cups[1],cups[2] = cups[2],cups[1]

for i in range(len(cups)) :
    if len(cups[i]) == 1 : 
        print(i + 1)
        break