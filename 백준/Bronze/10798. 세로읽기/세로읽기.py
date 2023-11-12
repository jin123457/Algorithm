words_arr = []
max_length = 0
min_length = 20
for _ in range(5) :
  arr = list(map(str,input()))
  if max_length < len(arr) :
    max_length = len(arr)
  if min_length > len(arr) :
    min_length = len(arr)
  words_arr.append(arr)

for i in range(0,max_length,1):
  for word in words_arr :
    if len(word) <= i: continue
    print(word[i],end="")