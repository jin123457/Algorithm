N = int(input())

arr = [[1,0],[0,1]]
    
for i in range(40) :
    arr.append([arr[-1][0] + arr[-2][0], arr[-1][1] + arr[-2][1]])

for j in range(N) :
    M = int(input())
    print(*arr[M])