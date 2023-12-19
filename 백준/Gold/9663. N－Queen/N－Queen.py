import sys
input = sys.stdin.readline

def chess_check(x,y) :
    for i in range(x):
        if A[i] == y or \
           A[i] == y + x - i or \
           A[i] == y - x + i:
            return False
        
    return True

def dfs(row) :
    global ans
    if row == N :
        ans += 1
        return
    
    for col in range(N) :
        if chess_check(row,col) :
            A[row] = col
            dfs(row + 1)

N = int(input())
A = [0] * N 
ans = 0

dfs(0)
print(ans)