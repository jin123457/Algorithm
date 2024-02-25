import sys

input = sys.stdin.readline

def paper_cut(x,y,n) :
    global m,z,p

    color = paper[x][y]
    
    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if color != paper[i][j] :
                paper_cut(x, y, n//3)
                paper_cut(x, y+n//3, n//3)
                paper_cut(x, y + n//3 + n//3, n//3)
                paper_cut(x + n//3, y, n//3)
                paper_cut(x + n//3, y+n//3, n//3)
                paper_cut(x + n//3, y + n//3 + n//3, n//3)
                paper_cut(x + n//3 + n//3, y, n//3)
                paper_cut(x + n//3 + n//3, y+n//3, n//3)
                paper_cut(x + n//3 + n//3, y + n//3 + n//3, n//3)
                return
    if color == -1 :
        m += 1
    elif color == 0 :
        z += 1
    else :
        p += 1

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
m = z = p = 0

paper_cut(0,0,N)
print(m,z,p,sep="\n")