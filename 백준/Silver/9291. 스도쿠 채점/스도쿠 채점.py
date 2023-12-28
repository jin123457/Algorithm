import sys

input = sys.stdin.readline

def check_row(i,A) :
    sudoku = set()

    for j in range(9) :
        sudoku.add(A[i][j])
    
    if len(sudoku) < 9 :
         return False
    else :
        return True

def check_col(i,A) :
    sudoku = set()

    for j in range(9) :
        sudoku.add(A[j][i])
            
    if len(sudoku) < 9 :
         return False
    else :
        return True

def is_sudoku(A) :
    for i in range(9) :
        if not check_row(i,A) or not check_col(i,A) :
            return False
    for i in range(0,9,3) :
        for j in range(0,9,3) :
            check_box = set()
            for a in range(3) :
                for b in range(3) :
                    check_box.add(A[i + a][j + b]) 
            if len(check_box) < 9 :
                return False
    return True

N = int(input())

for i in range(N) :
    if i > 0 : input()

    A = list(list(map(int,input().split())) for _ in range(9))
    if is_sudoku(A) :
        print(f"Case {i + 1}: CORRECT")
    else :
        print(f"Case {i + 1}: INCORRECT")