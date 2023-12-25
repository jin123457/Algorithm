import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = deque(map(int,input().split()))
L = []
R = []
L.append(A.popleft())
R.append(A.popleft())

for i in A : 
    if sum(L) <= sum(R) :
        L.append(i)
    else :
        R.append(i)

mx = max(sum(L),sum(R))
mn = min(sum(L),sum(R))
total = 0

if mx != mn :
    df = mx - mn

    if df >= 100 :
       total += df // 100
       df %= 100

    if df >= 50 :
       total += df // 50
       df %= 50

    if df >= 20 :
       total += df // 20
       df %= 20

    if df >= 10 :
       total += df // 10
       df %= 10

    if df >= 5 :
       total += df // 5
       df %= 5

    if df >= 2 :
       total += df // 2
       df %= 2

    if df >= 1 :
       total += df // 1
       df %= 1

print(total)