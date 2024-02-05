import sys

input = sys.stdin.readline

N = int(input())
Y = 2019
M = [31,28,31,30,31,30,31,31,30,31,30,31]
YM = [31,29,31,30,31,30,31,31,30,31,30,31]
d = 3
ans = 0
for i in range(Y,N + 1) :
    if i % 400 == 0 or (i % 100 != 0 and i % 4 == 0) :
       for m in YM :
            is_fri = (12 + d) % 7
            if is_fri == 6 : ans += 1
            d = (m + d) % 7
    else :
        for m in M :
            is_fri = (12 + d) % 7
            if is_fri == 6 : ans += 1
            d = (m + d) % 7
print(ans)