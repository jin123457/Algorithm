str_name = input()
alpabet_arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpabet_arr_index = [-1 for _ in range(26)]
i = 0

for N in str_name :
  index = alpabet_arr.index(N)
  if alpabet_arr_index[index] == -1 :
    alpabet_arr_index[index] = i
  i += 1

alpabet_arr_index = map(str,alpabet_arr_index)
alpabet_arr_index = " ".join(alpabet_arr_index)
print(alpabet_arr_index)