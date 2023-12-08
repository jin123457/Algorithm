import sys

input = sys.stdin.readline

def combinations() :
    global N,M,ans
    if len(ans) == M :
        print(" ".join(list(map(str,ans))))
        return

    for i in range(1,N+1) :
        if i not in ans :
            if len(ans) >= 1 and ans[len(ans) - 1] > i : continue
            ans += [i]
            combinations()
            ans.pop()

N,M = map(int,input().split())
ans = []
combinations()