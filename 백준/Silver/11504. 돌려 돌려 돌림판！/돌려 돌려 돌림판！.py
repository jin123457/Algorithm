import sys

input = sys.stdin.readline

T = int(input())
ans = list()
for _ in range(T) :
    N,M = map(int,input().split())
    x = int(input().rstrip().replace(" ",""))
    y = int(input().rstrip().replace(" ",""))
    roulette = list(map(int,input().split()))
    total = 0
    arr = [[] for _ in range(N)]
    for i in range(N) :
        arr[i].append(roulette[i])
        for j in range(1,M) :
            target = (i + j) % N
            arr[i].append(roulette[target])

    for nm in arr :
        nm_change = int("".join(list(map(str,nm))))
        if x <= nm_change <= y :
            total += 1
    ans.append(total)

print(*ans,sep="\n")