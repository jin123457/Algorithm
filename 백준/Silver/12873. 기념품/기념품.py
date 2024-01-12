import sys

input = sys.stdin.readline

N = int(input())
A = [i for i in range(1,N + 1)]
before_target = 0
if len(A) > 1 :
    for i in range(1,N) :
        target = (i ** 3) % len(A) - 1 + before_target
        if target >= len(A) :
            target %= len(A)
        A.pop(target)
        if target < 0 :
            target = 0
        before_target = target
    print(A[0])
else :
    print(1)