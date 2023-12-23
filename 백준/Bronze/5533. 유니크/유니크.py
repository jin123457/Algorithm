import sys
input = sys.stdin.readline

def card_game(idx):
    
    for i in range(N) :
        is_uniq = True
        target = A[i][idx]
        for j in range(N) :
            if i == j : continue
            if target == A[j][idx] : is_uniq = False

        if is_uniq :
            ans[i] += target

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
ans = [0] * N

for i in range(3) :
    card_game(i)

print("\n".join(map(str,ans)))