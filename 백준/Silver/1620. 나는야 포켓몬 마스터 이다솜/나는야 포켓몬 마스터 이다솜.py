import sys
N,M = map(int,sys.stdin.readline().rstrip().split()) # 도감의 있는 포켓몬 개수는 N, 맞춰야하는 포켓문 문제의 개수는 M
pocketmon_obj = {} # 포켓몬들을 담을 도감 초기화
pocketmon_nm_obj = {} # 포켓몬들을 담을 도감 초기화
for i in range(1,N + M + 1) :
  # for문을 돌면서 도감 안에 포켓몬들을 넣는다. key값 : 포켓몬의 이름 value값 : 포켓몬의 번호
  pocketmon = sys.stdin.readline().rstrip()
  if N >= i :
    pocketmon_obj[pocketmon] = str(i)
    pocketmon_nm_obj[str(i)] = pocketmon
  else :
    # 문제를 하나하나 받아오면서 번호로 들어오는 경우는 포켓몬의 이름으로, 이름으로 들어오는 경우는 포켓몬의 번호를 출력한다.
    if pocketmon in pocketmon_obj :
      print(pocketmon_obj[pocketmon])
    elif pocketmon in pocketmon_nm_obj :
      print(pocketmon_nm_obj[pocketmon])