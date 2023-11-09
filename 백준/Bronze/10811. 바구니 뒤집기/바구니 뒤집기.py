N, M = map(int, input().split())

basket = [ n for n in range(0,N + 1)]
basket_position = [list(map(int,input().split())) for _ in range(M)]

def reverse_ball(i,j) :
    reverse_basket = basket[i:j+1]
    reverse_basket.reverse()
    basket[i:j+1] = reverse_basket


for basket_nm in basket_position :
  i,j = basket_nm
  reverse_ball(i,j)

basket.pop(0)
basket = map(str,basket)
basket = " ".join(basket)
print(basket)