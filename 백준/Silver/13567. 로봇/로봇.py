import sys

input = sys.stdin.readline

N,M = map(int,input().split())
dire = 'R'
coordinate = [0,0]
move_out = False
for i in range(M) :
    mv,nm = input().split()
    nm = int(nm)
    if mv == "TURN" :
        if dire == 'R':
            if nm == 0 :
                dire = "U"
            else :
                dire = "D"
        elif dire == 'L':
            if nm == 0 :
                dire = "D"
            else :
                dire = "U"
        elif dire == 'D':
            if nm == 0 :
                dire = "R"
            else :
                dire = "L"
        elif dire == 'U':
            if nm == 0 :
                dire = "L"
            else :
                dire = "R"
    else :
        if dire == "L" :
            coordinate[0] -= nm
        elif dire == "R" :
            coordinate[0] += nm
        elif dire == "U" :
            coordinate[1] += nm
        elif dire == "D" :
            coordinate[1] -= nm
    
    if coordinate[0] < 0 or coordinate[0] > N or coordinate[1] < 0 or coordinate[1] > N :
        move_out = True
        break
if move_out :
    print(-1)
else :
    print(*coordinate)