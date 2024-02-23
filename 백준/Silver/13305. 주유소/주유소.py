import sys

input = sys.stdin.readline

N = int(input())
oil = list(map(int,input().split()))
city = list(map(int,input().split()))
oil_cheep = min(city[:len(city) - 1])
oil_expensive = sys.maxsize
money = 0

for i in range(len(city) - 1) :

    if oil_cheep == city[i] :
        money += city[i] * sum(oil[i:])
        break

    if oil_expensive > city[i] :
        money += city[i] * oil[i]
        oil_expensive = city[i]
    else :
        money += oil_expensive * oil[i]
        
print(money)