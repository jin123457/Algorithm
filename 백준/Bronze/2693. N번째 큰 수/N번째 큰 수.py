import sys

input = sys.stdin.readline

N = 3
T = int(input())

for _ in range(T) :
    arr = sorted(list(map(int,input().split())))
    
    print(arr[-N])