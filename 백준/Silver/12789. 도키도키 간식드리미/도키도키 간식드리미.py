from collections import deque

T = int(input())

arr = deque(map(int,input().split()))
ans = deque()
i = 1
while len(arr) > 0:
    if len(ans) > 0 :
        if i == ans[-1] :
            ans.pop()
            i += 1
            continue

    out = arr.popleft()
    if i != out :
        ans.append(out)
    else : i += 1
    
for _ in range(len(ans)) :
    late_out = ans[-1]
    if i != late_out :
        break
    else :
        ans.pop()
        i +=1 

if len(ans) > 0 or len(arr) > 0 :
    print("Sad")
else :
    print("Nice")