import sys

N = int(sys.stdin.readline()) # 몇 개의 자연수를 배열의 받을 것인지에 대한 자연수
obj = {} # {} 초기화 선언
# for문을 돌면서 자연수를 x,y로 나눠서 받는게 좋기 때문에 {}에 넣는다.
for _ in range(N) :
  x,y = map(int,sys.stdin.readline().split()) # 받은 줄에 자연수를 두개를 x와 y의 나눠담는다.
  # y가 기준이 되므로 key 값에 y를 넣어준다.
  # obj 안에 key 값에 y가 없을 시, 배열을 선언하고 배열안에 x를 넣는다.
  # obj 안에 key 값에 y가 있을 시, 배열안에 x를 넣는다.
  if y not in obj :
    obj[y] = []
    obj[y].append(x)
  else :
    obj[y].append(x)
# obj를 key 값으로 오름차순 정렬을 한 후, key값을 하나씩 빼온다.
for nm in sorted(obj):
  obj[nm].sort() # value 안에 있는 배열을 정렬한다.
  # obj[nm] 길이가 1보다 길 경우, obj[nm]에 담겨 있는 배열을 하나씩 꺼내온다.
  # obj[nm] 길이가 1일 경우, obj[nm] 배열 첫번째 요소를 가지고 온다.
  if len(obj[nm]) > 1 :
    for i in obj[nm] :
      print(f"{i} {nm}")
  else :
    print(f"{obj[nm][0]} {nm}")
