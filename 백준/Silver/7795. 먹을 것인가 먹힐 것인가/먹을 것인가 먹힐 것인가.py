import sys

input = sys.stdin.readline

def binary_search(a,B) :
    S,E = 0,len(B) - 1
    total = -1
    while S <= E :
        mid = (S + E) // 2

        if B[mid] < a :
            total = mid
            S = mid + 1
        else :
            E = mid - 1
    
    return total

T = int(input())


for _ in range(T) :
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))
    ans = 0
    for a in A :
        ans += (binary_search(a,B) + 1)
    print(ans)