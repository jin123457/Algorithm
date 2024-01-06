import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = [sorted(list(map(int,input().split())),reverse=True) for _ in range(N)]
cards = [[] for _ in range(M)]
people = [0 for _ in range(N)]
ans = []

for i in range(M) :
  for j in range(N) :
    cards[i].append(A[j][i])

for card in cards :
  max_nm = max(card)
  for i in range(N) :
    if max_nm == card[i] :
      people[i] += 1

max_score = max(people)

for i in range(len(people)) :
  if max_score == people[i] :
    ans.append(i + 1)
print(*ans)