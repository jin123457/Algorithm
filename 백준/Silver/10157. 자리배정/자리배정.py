import sys

input = sys.stdin.readline

def assign(N,M,dire,point,R,C) :
    R -= 1
    flag = 0
    while N > M : 
        if dire[flag] == "up" :
            point[1] += C
            M += C
            C -= 1
            if M > N :
                point[1] -= (M - N)

        elif dire[flag] == "right" :
            point[0] += R
            M += R
            R -= 1
            if M > N :
                point[0] -= (M - N)

        elif dire[flag] == "down" :
            point[1] -= C
            M += C
            C -= 1
            if M > N :
                point[1] += (M - N)
        
        elif dire[flag] == "left" :
            point[0] -= R
            M += R
            R -= 1
            if M > N :
                point[0] += (M - N)

        flag = (flag + 1) % 4
        
    return point

R,C = map(int,input().split())
N = int(input())
M = 0
point = [1,0]
dire = ['up','right','down','left']
is_possible = True
if R * C < N :
    is_possible = False

if is_possible :
    print(*assign(N,M,dire,point,R,C))
else :
    print(0)