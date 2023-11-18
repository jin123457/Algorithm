import sys

N = int(sys.stdin.readline().rstrip()) # 나의 카드 개수
cards = list(map(int,sys.stdin.readline().rstrip().split())) # 내 카드의 숫자
M = int(sys.stdin.readline().rstrip()) # 다른 사람의 카드의 개수
card_arr = list(map(int,sys.stdin.readline().rstrip().split())) # 다른 사람의 카드의 숫자
my_card = {} # 내가 가진 카드를 {}에 담는다. {}에 담는 이유는 내 카드가 몇 번 중복되는지 알기 위해서 이다.
# for문을 돌면서 my_card에 넣어주기
for nm in card_arr :
  my_card[nm] = 0
# 다른 사람의 카드를 하나씩 꺼내면서 내 카드 안에 있으면 + 1씩 올려준다.
for card_nm in cards :
  if card_nm in my_card :
    my_card[card_nm] += 1
# 완성된 카드를 다른 사람의 카드와 비교하면서 value값을 출력한다.
for card_nm in card_arr :
    print(my_card[card_nm],end=" ")
print()