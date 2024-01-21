import sys

input = sys.stdin.readline

N = int(input())
M = sorted([int(input()) for _ in range(N)])
Y = [i for i in range(1,(2 * N) + 1) if not i in M]
A = []
turn = "M"
target = 0
while True :
    if len(M) == 0 or len(Y) == 0 : break

    if turn == "M" : arr = M
    else : arr = Y
    

    possible_card = [i for i in arr if i > target]
    if(len(possible_card)) :
        mn_card = min(possible_card)
        arr.remove(mn_card)
        A.append(mn_card)
        turn = "Y" if turn == "M" else "M"
        target = mn_card
    else :
        A = []
        target = 0
        if turn == "Y" : arr = M
        else : arr = Y
        card = arr.pop(0)
        A.append(card)
        target = card

print(len(Y),len(M),sep="\n")