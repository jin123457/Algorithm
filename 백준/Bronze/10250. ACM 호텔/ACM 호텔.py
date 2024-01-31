import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    H,W,N = map(int,input().split())
    if N % H == 0 : 
        col = H
        row = N // H
    else :
        col = N % H
        row = (N // H) + 1
    if row > 9 :
        print(f"{col}{row}")
    else :
        print(f"{col}0{row}")