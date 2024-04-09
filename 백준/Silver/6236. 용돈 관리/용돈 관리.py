import sys

input = sys.stdin.readline

N,M = map(int,input().split())
A = list(int(input()) for _ in range(N))
S,E = min(A),sum(A)
ans = 0

while S <= E :
    mid = (S + E) // 2
    withdraw = 1
    money = mid
    for a in A :
        if money < a :
            money = mid
            withdraw += 1
        money -= a

    if withdraw > M or mid < max(A) :
        S = mid + 1
    else :
        E = mid - 1
        ans = mid
    
print(ans)