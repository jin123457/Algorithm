N,M = map(int,input().split()) 
str_arr = [input() for _ in range(N + M)]
str_obj = set()
count = 0

for i in range(N + M) :
  if N > i :
    str_obj.add(str_arr[i])
  else :
    if str_arr[i] in str_obj :
      count += 1
    
print(count)