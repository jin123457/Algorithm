arr = [] # 소인수를 담을 배열 초기화

# 소인수 분해를 하는 함수 선언 파라미터로 초기값을 받는다.
def factors(nm) :
  i = 2 # 소인수 분해를 하기 전에 제일 작은 소수 2를 선언한다.
  # nm이 1보다 클 때까지 무한 반복을 한다. 1은 소수가 아니기 떄문에 1을 기준으로 삼는다.
  while nm > 1 :
    # nm % i == 0 일 경우 해당 i는 소수이기 때문에 arr 배열에 i를 담아주고 nm를 i로 나눈 몫을 nm으로 교체해준다.
    if nm % i == 0 :
      arr.append(i)
      nm //= i
    else :
      # nm % i == 0 아닐 경우 i는 소수가 아니므로 +1을 해줘서 다음 수가 소수인지 확인을 한다.
      i += 1
  return arr # arr배열을 리턴해준다.
# 함수는 종료 후 arr 배열을 리턴하므로, arr 배열 안에 있는 소인수를 하나씩 꺼내온다.
for number in factors(int(input())) :
  print(number)