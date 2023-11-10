N = 9
arr = [list(map(int,input().split())) for _ in  range(N)]
nm_info = {}
max_nm_arr = []


for i in range(len(arr)) :
  max_nm_arr.append(max(arr[i]))
  nm_info[max(arr[i])] = [i + 1,arr[i].index(max(arr[i])) + 1]

nm_info[max(max_nm_arr)] = map(str,nm_info[max(max_nm_arr)])
max_nm_index = nm_info[max(max_nm_arr)] = " ".join(nm_info[max(max_nm_arr)])
print(max(max_nm_arr))
print(max_nm_index)