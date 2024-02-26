import sys

input = sys.stdin.readline

def DAC(x,y,n) :
    global zero,one,ans

    is_zero = board[x][y]

    for i in range(x,x + n) :
        for j in range(y,y + n) :
            if is_zero != board[i][j] :
                ans.append('(')
                DAC(x, y, n // 2)
                DAC(x, y + n // 2, n // 2)
                DAC(x + n // 2, y, n // 2)
                DAC(x + n // 2, y + n // 2, n // 2)
                ans.append(')')
                return
            
    if is_zero == 0 :
        ans.append('0')
    else :
        ans.append('1')

N = int(input())
board = [list(map(int,list(input().rstrip()))) for _ in range(N)]
ans = []
zero = one = 0
DAC(0,0,N)
print("".join(ans))