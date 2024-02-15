import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
ans = 0
total = 0
stiker = [0] * 100001

for a in arr :
    if not stiker[a] :
        stiker[a] = 1
        total += 1
    else :
        total -= 1
    
    if ans < total :
        ans = total
print(ans)
