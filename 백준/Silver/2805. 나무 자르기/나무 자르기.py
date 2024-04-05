def binary_search(A,L) :
    S,E = 1,max(A)

    while S <= E :
        mid = (S + E) // 2
        tree = 0
        
        for a in A :
            if a > mid :
                tree += a - mid
                
        if tree >= L :
            S = mid + 1
        else :
            E = mid - 1
    return E

N,M = map(int,input().split())
arr = list(map(int,input().split()))


print(binary_search(arr,M))