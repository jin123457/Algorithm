import sys

input = sys.stdin.readline

N,M = map(int,input().split())
image = [list(map(int,input().split())) for _ in range(N)]
SFilter = 0
EFilter = 2
ans = []
T = int(input())

for i in range(N - 2) :
  for j in range(M - 2) :
    arr = []
    arr.append(image[i][j])
    arr.append(image[i + 1][j])
    arr.append(image[i + 2][j])
    arr.append(image[i][j + 1])
    arr.append(image[i][j + 2])
    arr.append(image[i + 1][j + 1])
    arr.append(image[i + 1][j + 2])
    arr.append(image[i + 2][j + 1])
    arr.append(image[i + 2][j + 2])
    ans.append(sorted(arr)[4])

total = 0
for a in ans : 
  if a >= T : total += 1
  
print(total)