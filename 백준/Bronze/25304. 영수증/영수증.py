import sys

Total = int(sys.stdin.readline())
Cnt = int(sys.stdin.readline())
priceTotal = 0

for i in range(Cnt) :
  price,itemCnt = map(int,sys.stdin.readline().split())
  priceTotal += price * itemCnt

if priceTotal == Total :
  print('Yes')
else :
  print('No')