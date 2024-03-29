import sys

input = sys.stdin.readline

def paper_cut(x,y,n) :
    global white,blue

    color = paper[x][y]
    
    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if color != paper[i][j] :
                paper_cut(x, y, n//2)
                paper_cut(x, y+n//2, n//2)
                paper_cut(x+n//2, y, n//2)
                paper_cut(x+n//2, y+n//2, n//2)
                return
    if color == 0 :
        white+= 1
    else :
        blue+= 1

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
white = blue = 0

paper_cut(0,0,N)
print(white,blue,sep="\n")