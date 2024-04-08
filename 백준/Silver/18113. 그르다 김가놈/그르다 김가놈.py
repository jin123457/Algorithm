import sys

input = sys.stdin.readline

def binary_search(A,T) :
    S,E = 1,max(A)
    ans = -1
    while S <= E :
        mid = (S + E) // 2
        total = 0
        for a in A :
            total += (a // mid)
            
        if total >= T :
            S = mid + 1
            ans = max(ans,mid)
        else :
            E = mid - 1

    return ans

N,K,M = map(int,input().split())
arr = []
for _ in range(N) :
    tmp = int(input())
    if tmp < 2 * K and tmp - K > 0:
        arr.append(tmp-K)
    elif tmp > 2 * K :
        arr.append(tmp-2 * K)

if len(arr) == 0 :
    print(-1)
else :
    print(binary_search(arr,M))