import sys
A,B,C,D,E,F = map(int, sys.stdin.readline().split()) # 자연수를 int형으로 변환시켜 각각에 변수에 담아준다.
# for문을 두번 돌리면서 i와 j의 모든 경우의 수를 알아본다.
for i in range(-999,1000) :
  for j in range(-999,1000) :
    # AX + BY = C와 DX + EY = F의 공식이 일치하는 i와 를 출력하고 멈춰준다.
    if (A * i) + (B * j) == C and(D * i) + (E * j) == F :
      print(i,j)
      break