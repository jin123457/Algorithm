N = int(input())
arr = list(input().rstrip())
target = 0
is_true = True
for a in arr :
    if target == a :
        is_true = False
        break
    else :
        target = a
if is_true :
    print('Yes')
else :
    print('No')