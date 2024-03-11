for _ in range(3) :
    arr = sum(map(int,input().split()))
    if arr == 1 :
        print('C')
    elif arr == 2 :
        print('B')
    elif arr == 3 :
        print('A')
    elif arr == 4 :
        print('E')
    elif arr == 0 :
        print('D')