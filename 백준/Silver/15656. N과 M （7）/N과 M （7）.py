import sys

input = sys.stdin.readline

def combinations() :
    global N,M,ans,arr
    if len(ans) == M :
        print(" ".join(list(map(str,ans))))
        return

    for i in sorted(arr) :
        ans += [i]
        combinations()
        ans.pop()

N,M = map(int,input().split())
arr = list(map(int,input().split()))
ans = list()
combinations()