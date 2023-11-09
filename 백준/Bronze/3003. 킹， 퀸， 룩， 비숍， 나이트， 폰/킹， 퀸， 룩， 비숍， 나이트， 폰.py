perpect_toy = [1,1,2,2,2,8]
my_toy = list(map(int,input().split()))
need_toy = [0 for _ in range(6)]

for i in range(len(perpect_toy)) :
  need_toy[i] = perpect_toy[i] - my_toy[i]

need_toy = map(str,need_toy)
need_toy = " ".join(need_toy)
print(need_toy)