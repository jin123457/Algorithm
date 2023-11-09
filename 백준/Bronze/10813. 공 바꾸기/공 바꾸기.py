N, M = map(int, input().split())

basket = [ n for n in range(0,N + 1)]
basket_position = [list(map(int,input().split())) for _ in range(M)]

def change_ball(i,j) :
    target_basket = basket[i]
    basket[i] = basket[j]
    basket[j] = target_basket


for basket_nm in basket_position :
  i,j = basket_nm
  change_ball(i,j)

basket.pop(0)
basket = map(str,basket)
basket = " ".join(basket)
print(basket)