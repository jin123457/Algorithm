import sys

input = sys.stdin.readline

N,M = map(int,input().split())
road = [[] for _ in range(N)]
for i in range(N) :
    km,spped = map(int,input().split())
    if i == 0 :
        road[i].append(0)
        road[i].append(km)
        road[i].append(spped)
    else :
        road[i].append(road[i - 1][1] + 1)
        road[i].append(road[i - 1][1] + km)
        road[i].append(spped)
me = [[] for _ in range(M)]
for i in range(M) :
    km,spped = map(int,input().split())
    if i == 0 :
        me[i].append(0)
        me[i].append(km)
        me[i].append(spped)
    else :
        me[i].append(me[i - 1][1] + 1)
        me[i].append(me[i - 1][1] + km)
        me[i].append(spped)

km = 1
me_position = 0
road_position = 0
violation = 0
while True :
    if km == 101 : break

    if road[road_position][1] < km : 
        road_position += 1

    if me[me_position][1] < km : 
        me_position += 1

    km += 1
    violation = max(violation,me[me_position][2] - road[road_position][2])

print(violation)