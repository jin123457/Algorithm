import sys
from collections import deque

input = sys.stdin.readline

N,W,L = map(int,input().split())
arrive = list()
brige = deque(0 for _ in range(W))
trucks = list(map(int,input().split()))
time = 0
brige_weight = 0
i = 0
while len(arrive) < N :
    if i == N :
        out = brige.popleft()
        
        if out > 0 :
            arrive.append(out)

        brige.append(0)
    else :
        out = brige.popleft()
        if out > 0 :
            arrive.append(out)

        brige_weight = sum(brige)    

        if brige_weight + trucks[i] <= L :
            brige.append(trucks[i])
            i += 1
        else :
           brige.append(0)

    time += 1
print(time)