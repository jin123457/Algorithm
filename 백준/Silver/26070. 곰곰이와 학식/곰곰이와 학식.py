import sys

input = sys.stdin.readline

A,B,C = map(int,input().split())
X,Y,Z = map(int,input().split())
total = 0
for i in range(3) :
    chicken = min(A,X)
    total += chicken
    A -= chicken
    X -= chicken

    pizza = min(B,Y)
    total += pizza
    B -= pizza
    Y -= pizza

    hambuger = min(C,Z)
    total += hambuger
    C -= hambuger
    Z -= hambuger

    Y,Z,X = X // 3,Y // 3,Z // 3

print(total)