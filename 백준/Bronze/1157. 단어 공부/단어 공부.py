string = input().upper()
str_arr = set()
all_str_arr = list(string)
count_arr = {}
for i in range(len(string)) :
  str_arr.add(string[i])

for arr in str_arr :
  count_arr[arr] =all_str_arr.count(arr)

tmp = [k for k,v in count_arr.items() if max(count_arr.values()) == v]

if len(tmp) > 1 :
  print('?')
else :
  tmp = map(str,tmp)
  tmp = "".join(tmp)
  print(tmp) 