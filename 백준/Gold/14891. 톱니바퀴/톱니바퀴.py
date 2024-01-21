import sys
from collections import deque

input = sys.stdin.readline

cogwheel = [deque(input().rstrip()) for _ in range(4)]
N = int(input())

for _ in range(N) :
    nm,dire = map(int,input().split())
    is_spin = []
    for i in range(3) :
        if cogwheel[i][2] == cogwheel[i + 1][6] :
            is_spin.append(False)
        else :
            is_spin.append(True)
    if nm == 1 :
        cogwheel[0].rotate(dire)
        for i,spin in enumerate(is_spin) :
            if spin == False : break

            if i == 0 :
                cogwheel[1].rotate(-dire)
            elif i == 1 :
                cogwheel[2].rotate(dire)
            elif i == 2 :
                cogwheel[3].rotate(-dire)
    elif nm == 2 :
        cogwheel[1].rotate(dire)
        if is_spin[0] :
            cogwheel[0].rotate(-dire)
        if is_spin[1] :
            cogwheel[2].rotate(-dire)
        if is_spin[1] and is_spin[2] :
            cogwheel[3].rotate(dire)
    elif nm == 3 :
        cogwheel[2].rotate(dire)
        if is_spin[0] and is_spin[1] :
            cogwheel[0].rotate(dire)
        if is_spin[1] :
            cogwheel[1].rotate(-dire)
        if is_spin[2] :
            cogwheel[3].rotate(-dire)
    elif nm == 4 :
        cogwheel[3].rotate(dire)
        for i,spin in enumerate(is_spin[::-1]) :
            if spin == False : break
            if i == 0 :
                cogwheel[2].rotate(-dire)
            elif i == 1 :
                cogwheel[1].rotate(dire)
            elif i == 2 :
                cogwheel[0].rotate(-dire)
total = 0
for i,wheel in enumerate(cogwheel) :
    if i == 0 and wheel[0] == "1":
        total += 1
    elif i == 1 and wheel[0] == "1":
        total += 2
    elif i == 2 and wheel[0] == "1":
        total += 4
    elif i == 3 and wheel[0] == "1":
        total += 8
print(total)