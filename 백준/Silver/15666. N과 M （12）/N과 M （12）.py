import sys

input = sys.stdin.readline

def combinations() :
    global N,M,ans,arr
    if len(ans) == M :
        print(" ".join(list(map(str,ans))))
        return
    for i in sorted(list(arr)) :
        #print(arr)
        if len(ans) >= 1 and ans[len(ans) - 1] > i :continue
        ans += [i]
        combinations()
        ans.pop()

N,M = map(int,input().split())
arr = set(map(int,input().split()))
ans = list()
combinations()