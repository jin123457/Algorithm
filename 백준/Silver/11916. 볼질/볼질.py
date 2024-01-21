import sys

input = sys.stdin.readline

N = int(input()) # 창석이가 던진 공의 수
balls = list(map(int,input().split())) # 던진 공의 종류를 담고 있는 배열
ball_count = 0 # 볼이 몇 번 왔는지 확인하는 카운터
base = [0 for _ in range(3)] # 베이스를 나타내는 배열
score = 0 # 점수
for B in balls :
    if B == 1 or B == 3 : ball_count += 1 
    else : ball_count = 0

    if B == 1 :
        if ball_count == 4 :
            ball_count = 0
            for i in range(len(base) - 1,-1,-1) :
                if i == 0 : base[0] =  1
                elif i == 2 and base[0] == 1 and base[1] == 1 and base[2] == 1 : score += 1
                else :
                    if i == 2 and base[0] == 1 and base[1] == 1 : base[i] = 1
                    elif i == 1 and base[0] == 1: base[i] = 1
    elif B == 2 :
        for i in range(len(base) - 1,-1,-1) :
            if i == 0 : base[0] =  1
            elif i == 2 and base[0] == 1 and base[1] == 1 and base[2] == 1 : score += 1
            else :
                if i == 2 and base[0] == 1 and base[1] == 1 : base[2] = 1
                elif i == 1 and base[0] == 1: base[1] = 1
    elif B == 3 :
        for i in range(len(base) - 1,-1,-1) :
            if i == 2 and base[2] == 1 : 
                base[2] = 0
                score += 1
            elif i == 1 and base[1] == 1 : 
                base[2] = 1
                base[1] = 0
            elif i == 0 and base[0] == 1: 
                base[1] = 1
                base[0] = 0
            else : 
                base[i] = 0
        if ball_count == 4 :
            ball_count = 0
            base[0] = 1 
print(score)