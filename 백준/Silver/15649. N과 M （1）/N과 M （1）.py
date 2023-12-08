import sys

def combinations() :
    global N,M,ans
    if len(ans) == M :
        print(" ".join(list(map(str,ans))))
        return

    for i in range(1,N+1) :
        if i not in ans :
            ans += [i]
            combinations()
            ans.pop()

N,M = map(int,input().split())
ans = []
combinations()