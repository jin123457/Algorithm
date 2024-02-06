import sys

input = sys.stdin.readline

N,M = map(int,input().split())
R,C,D = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
clean_room = 0
while True :

    if room[R][C] == 0 :
        clean_room += 1
        room[R][C] = 2

    if room[R - 1][C] != 0 and room[R + 1][C] != 0 and room[R][C -1] != 0 and room[R][C + 1] != 0 :
        if D == 0 :
            R += 1
        elif D == 1 :
            C -= 1
        elif D == 2 :
            R -= 1
        elif D == 3 :
            C += 1
        if room[R][C] == 1 : break
    else :
        if D == 0 : D += 3
        else : D -= 1

        if D == 0 :
            if room[R - 1][C] == 0 :
                R -= 1
        elif D == 1 :
            if room[R][C + 1] == 0 :
                C += 1
        elif D == 2 :
            if room[R + 1][C] == 0 :
                R += 1
        elif D == 3 :
            if room[R][C - 1] == 0 :
                C -= 1
print(clean_room)