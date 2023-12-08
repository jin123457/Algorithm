import sys

input = sys.stdin.readline

def combinations() :
    global N,M,ans
    if len(ans) == M :
        print(" ".join(list(map(str,ans))))
        return

    for i in range(1,N+1) :
        ans += [i]
        combinations()
        ans.pop()

N,M = map(int,input().split())
ans = []
combinations()