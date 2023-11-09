nm_arr = list(map(str,input().split()))
reverse_arr = []

for nm in nm_arr :
  list_nm = list(nm)
  list_nm.reverse()
  list_nm = "".join(list_nm)
  reverse_arr.append(list_nm)

print(max(reverse_arr))