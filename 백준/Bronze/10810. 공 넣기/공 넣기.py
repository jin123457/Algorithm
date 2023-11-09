N, M = map(int, input().split())

basket = [ 0 for _ in range(N + 1)]
ball_info = [list(map(int,input().split())) for _ in range(M)]

def into_ball(i,j,k) :
  for n in range(i,j +1,1) :
    basket[n] = k

for ball in ball_info :
  i,j,k = ball
  into_ball(i,j,k)

basket.pop(0)
basket = map(str,basket)
basket = " ".join(basket)
print(basket)