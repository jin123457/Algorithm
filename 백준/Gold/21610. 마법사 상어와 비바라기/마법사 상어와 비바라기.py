import sys

input = sys.stdin.readline

def move_clude(D,S,C) :
    mv = [(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

    for i in range(len(C)) :
        new_r,new_c = C[i]
        r,c = mv[D]
        if r != 0 :
            new_r += r * S
            new_r %= N
        if c != 0 :
            new_c += c * S
            new_c %= N
        C[i] = (new_r,new_c)
    return C

def make_cloude(C) :
    global board

    cloudes = []
    for i in range(N) :
        for j in range(N) :
            if board[i][j] > 1 and (i,j) not in C :
                cloudes.append((i,j))
                board[i][j] -= 2
    return cloudes

def plus_water(C) :
    global board

    check_mv = [(-1,-1),(-1,1),(1,1),(1,-1)]
    for rain in sorted(C) :
        r,c = rain
        total = 0
        for cm in check_mv :
            new_r = r + cm[0]
            new_c = c + cm[1]
            
            if 0 <= new_r < N and 0 <= new_c < N :
                if board[new_r][new_c] : total += 1
        board[r][c] += total

def rain(C) :
    global board
    
    
    for rain in sorted(C) :
        r,c = rain
        board[r][c] += 1

    plus_water(C)   
    

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
cloudes = [(N-2, 0),(N-2, 1),(N-1, 0),(N-1, 1)]

for _ in range(M) :
    D,S = map(int,input().split())
    
    C = move_clude(D,S,cloudes)
    rain(C)
    cloudes = make_cloude(C)

ans = 0
for i in range(N) :
    for j in range(N) :
        ans += board[i][j]
print(ans)