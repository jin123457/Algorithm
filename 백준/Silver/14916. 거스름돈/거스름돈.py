import sys

input = sys.stdin.readline

N = int(input())
is_paied = False
for i in range(N // 5,-1,-1) :
    if (N - 5 * i) % 2 == 0 :
        print(i + ((N - 5 * i) // 2))
        is_paied = True
        break

if not is_paied :
    print(-1)