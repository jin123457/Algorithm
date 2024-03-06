arr = ['a','i','u','e','o']

input()
N = list(input().rstrip())
ans = 0

for n in N :
    if n in arr : ans += 1
        
print(ans)