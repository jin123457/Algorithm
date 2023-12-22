import sys

input = sys.stdin.readline

N,M = map(int,input().split())
ans = list()
number = 0
while len(ans) < N :
  number += 1
  nm_list = [int(i) for i in str(number)]
  if M in nm_list  : continue

  ans.append(number)
  nm_list = list()
  
print(ans[-1])