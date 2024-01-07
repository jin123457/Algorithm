import sys

input = sys.stdin.readline

N = int(input())
mvs = input()
A = [['.'] * N for _ in range(N)]
start = [0,0]
for mv in mvs :
    x,y = start
    
    if mv == "D" :
        if x + 1 > N - 1 : continue

        if A[x][y] == "-" :
            A[x][y] = "+"
        elif A[x][y] == "." :
            A[x][y] = "|" 

        if A[x + 1][y] == "-" :
            A[x + 1][y] = "+"
        elif A[x + 1][y] == "." :
            A[x + 1][y] = "|" 
        start[0] += 1

    if mv == "U" :
        if x - 1 < 0 : continue

        if A[x][y] == "-" :
            A[x][y] = "+"
        elif A[x][y] == "." :
            A[x][y] = "|" 

        if A[x - 1][y] == "-" :
            A[x - 1][y] = "+"
        elif A[x - 1][y] == "." :
            A[x - 1][y] = "|" 
        start[0] -= 1

    if mv == "R" :
        if y + 1 > N - 1 : continue

        if A[x][y] == "|" :
            A[x][y] = "+"
        elif A[x][y] == "." :
            A[x][y] = "-" 

        if A[x][y + 1] == "|" :
            A[x][y + 1] = "+"
        elif A[x][y + 1] == "." :
            A[x][y + 1] = "-" 
        start[1] += 1

    if mv == "L" :
        if y - 1 < 0 : continue

        if A[x][y] == "|" :
            A[x][y] = "+"
        elif A[x][y] == "." :
            A[x][y] = "-" 

        if A[x][y - 1] == "|" :
            A[x][y - 1] = "+"
        elif A[x][y - 1] == "." :
            A[x][y - 1] = "-" 
        start[1] -= 1
    
for i in range(len(A)) :
    print(*A[i],sep="")