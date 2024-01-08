import sys

input = sys.stdin.readline

R,C = map(int,input().split())
A = [['.'] * (C + 2)]
mvs = [(1,0),(0,1),(-1,0),(0,-1)]
for _ in range(R) :
    maps = ['.'] + list(map(str,input().rstrip())) + ['.']
    A.append(maps)

A.append(['.'] * (C + 2))
new_A = [arr[:] for arr in A]
for i in range(R + 2) :
    for j in range(C + 2) :
        if A[i][j] == "X" :
            total = 0
            for mv in mvs :
                x,y = mv
                if A[i + x][j + y] == "." :
                    total += 1
            if total >= 3 :
                new_A[i][j] = "."

def col_check(new_A) :
    nm = set()
    for i in range(len(new_A)) :
        if new_A[i].count('X') > 0 : nm.add(i)
    front_nm = min(nm)
    back_nm = max(nm)

    for i in range(len(new_A) - 1,-1,-1) :
        if front_nm > i or back_nm < i:
            del new_A[i]

def row_check(new_A) :
    nm = set()
    for i in range(len(new_A[0])) :
        total = 0
        for j in range(len(new_A)):
            if new_A[j][i] == 'X':
                total += 1
        if total :
            nm.add(i)
    front_nm = min(nm)
    back_nm = max(nm)
    for i in range(len(new_A[0]) - 1,-1,-1) :
        if front_nm > i or back_nm < i:
            for j in range(len(new_A)) :
                del new_A[j][i]
col_check(new_A)
row_check(new_A)
for i in range(len(new_A)) :
    print("".join(new_A[i]))