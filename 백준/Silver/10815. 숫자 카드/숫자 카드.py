N = int(input()) # 나의 카드 개수
cards = list(map(int,input().split())) # 내 카드의 숫자
M = int(input()) # 다른 사람의 카드의 개수
card_arr = list(map(int,input().split())) # 다른 사랑의 카드의 숫자
my_card = set() # 내가 가진 카드를 set에 담는다. set을 하는 이유는 중복적으로 가지고 있는 카드를 들고 있을 필요가 없어서이다.
# for문을 돌면서 set에 넣어주기
for nm in cards :
  my_card.add(nm)
# 다른 사람의 카드를 하나씩 꺼내면서 내 카드 안에 있는지 확인하기 있으면 1 없으면 0
for card_nm in card_arr :
  if card_nm in my_card :
    print(1,end=" ")
  else :
    print(0,end=" ")
print()