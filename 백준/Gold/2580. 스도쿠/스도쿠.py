import sys
input = sys.stdin.readline

input = sys.stdin.readline

sudoku = list(list(map(int,input().split())) for _ in range(9))
blank = list()

for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 :
            blank.append((i,j))

def sudokuRow(x,a) :
    for i in range(9) :
        if a == sudoku[x][i] :
            return False
    return True

def sudokuCol(y,a) :
    for i in range(9) :
        if a == sudoku[i][y] :
            return False
    return True

def sudokuRect(x,y,a) :
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if a == sudoku[nx + i][ny + j] :
                return False
    return True

def dfs(idx) :
    if len(blank) == idx :
        for i in range(9) :
            print(*sudoku[i])
        exit(0)
    
    for i in range(1,10) :
        x = blank[idx][0]
        y = blank[idx][1]

        if sudokuRow(x,i) and sudokuCol(y,i) and sudokuRect(x,y,i) :
                sudoku[x][y] = i
                dfs(idx + 1)
                sudoku[x][y] = 0
dfs(0)