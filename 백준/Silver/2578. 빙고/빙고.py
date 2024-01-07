import sys

input = sys.stdin.readline

def row_check() :
    bingo_time = 0
    for i in range(5) :
        if sum(board[i]) == 0 :
            bingo_time += 1

    return bingo_time

def col_check() :
    bingo_time = 0

    for i in range(5) :
        total = 0
        for j in range(5) :
            total += board[j][i]

        if total == 0 : bingo_time += 1

    return bingo_time

def diagonal_check() :
    bingo_time = 0

    L_diagonal = 0
    R_diagonal = 0
    num = 4

    for i in range(5) :
        L_diagonal += board[i][i]
    
    for i in range(5) :
        R_diagonal += board[i][num]
        num -= 1

    if L_diagonal == 0 : bingo_time += 1
    if R_diagonal == 0 : bingo_time += 1

    return bingo_time


def bingo(num,time) :
    global bingo_finish
    is_find = False
    bingo_time = 0
    for i in range(5) :
        for j in range(5) :
            if board[i][j] == num :
                is_find = True
                board[i][j] = 0
                break
        if is_find : break
    
    bingo_time += row_check()
    bingo_time += col_check()
    bingo_time += diagonal_check()
    
    if bingo_time >= 3 : 
        bingo_finish = True
        print(time)

board = [list(map(int,input().split())) for _ in range(5)]
sayed = [list(map(int,input().split())) for _ in range(5)]
bingo_finish = False
time = 0
is_find = False
for i in range(5) :
    for j in range(5) :
        time += 1
        if not bingo_finish :
            bingo(sayed[i][j],time)
    if bingo_finish : break