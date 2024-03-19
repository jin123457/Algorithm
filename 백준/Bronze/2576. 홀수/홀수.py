ans = []

for _ in range(7) :
    N = int(input())

    if N % 2 == 1 :
        ans.append(N)
if len(ans) > 0 :
    print(sum(ans))
    print(min(ans))
else :
    print(-1)