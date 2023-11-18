import sys
N,M = map(int,sys.stdin.readline().split())
people_arr = [sys.stdin.readline().rstrip() for _ in range(N + M)]
people_arr1 = []
people_arr2 = set()
for i in range(len(people_arr)) :
  if i < N :
   people_arr2.add(people_arr[i])

  if i >= N :
    if people_arr[i] in people_arr2 :
      people_arr1.append(people_arr[i])
print(len(people_arr1))
for people in sorted(people_arr1) :
  print(people)