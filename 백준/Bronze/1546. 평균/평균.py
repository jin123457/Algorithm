N = int(input())
test_score = list(map(int,input().split()))
max_score = max(test_score)
new_score_arr = []


for score in test_score :
  new_score_arr.append(score / max_score * 100)

print(sum(new_score_arr) / N)