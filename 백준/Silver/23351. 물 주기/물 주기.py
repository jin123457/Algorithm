import sys

input = sys.stdin.readline

N,K,A,B = map(int,input().split())
flowerpot = [K] * N
target = 0
day = 0
while True :
    if 0 in flowerpot : break
    flowerpot[target:target + A] = [i + B for i in flowerpot[target:target + A]]
    flowerpot[0:N] = [i - 1 for i in flowerpot[0:N]]
    day += 1
    target = (target + A) % N
print(day)