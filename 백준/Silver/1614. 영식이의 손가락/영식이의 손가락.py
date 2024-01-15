import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
ans = 0
if M == 0 :
    ans = N - 1
else :
    target = N - 1
    if N == 1 :
        ans = 8 * M + target
    elif  N == 2 :
        target1 = M % 2
        if M > 1 :
            target2 = (M // 2) * 6
            target3 = (M // 2) * 2

            target4 = target2 + target3
            if target1 == 1 :
                ans = target + target4 + 6
            else :
                ans = target + target4
        else :
            target2 = 1 * 6
            ans = target + target2
        
    elif  N == 3 :
        ans = 4 * M + target
    elif  N == 4 :
        target1 = M % 2
        
        if M > 1 :
            target2 = (M // 2) * 2
            target3 = (M // 2) * 6
            target4 = target2 + target3
        
            if target1 == 1 :
                ans = target + target4 + 2
            else :
                ans = target + target4
        else :
            target2 = 1 * 2
            ans = target + target2
        
    elif N == 5 :
        ans = 8 * M + target
print(ans)