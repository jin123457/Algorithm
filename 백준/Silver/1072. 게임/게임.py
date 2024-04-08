import sys

input = sys.stdin.readline

X,Y = map(int,input().split())
Z = (Y * 100) // X

if Z > 98 :
    print(-1)
else :
    S = 0
    E = X
    ans = sys.maxsize
    while S <= E :
        mid = (S + E) // 2

        CZ = ((Y + mid) * 100) // (X + mid)

        if CZ > Z :
            ans = min(ans,mid)
            E = mid - 1
        else :
            S = mid + 1
    
    print(ans)