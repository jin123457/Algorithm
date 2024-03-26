N,M = map(int,input().split())
T = int(input()) * 2

if N + M >= T :
    print(N + M - T)
else :
    print(N + M)