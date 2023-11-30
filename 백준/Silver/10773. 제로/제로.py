T = int(input())
ans = []

for _ in range(T) :
    N = int(input())

    if N == 0 :
        ans.pop()
    else :
        ans.append(N)

print(sum(ans))