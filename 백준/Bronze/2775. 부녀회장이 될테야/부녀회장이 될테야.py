import sys

input = sys.stdin.readline

N = int(input())
APT = []
floor = []
room = []
max_floor = 0
max_room = 0
for _ in range(N) :
    my_floor = int(input())
    my_room = int(input())
    floor.append(my_floor)
    room.append(my_room)
    max_floor = max(floor)
    max_room = max(room)

APT = [[i for i in range(1,max_room + 1)]]

for _ in range(max_floor) :
    APT.append([])

for i in range(1,max_floor + 1) :
    for j in range(max_room) :
        if j == 0 :
            APT[i].append(APT[i - 1][j])
        else :
            APT[i].append(APT[i][j - 1] + APT[i - 1][j])

for i in range(N) :
    print(APT[floor[i]][room[i] - 1])