import sys

N = list(map(int,sys.stdin.readline().split()))
M = list(map(int,sys.stdin.readline().split()))
numerator = 0
numerator_arr = [N[0],M[0]]
denominator_arr = [N[1],M[1]]

def LCM(a,b,gcd) :
  return (a * b) // gcd

def GCD(a,b) :
  while b > 0 :
    a,b = b,a % b
  return a

max_nm = max(denominator_arr)
min_nm = min(denominator_arr)

lcm = LCM(min_nm,max_nm,GCD(max_nm,min_nm))

for i in range(len(numerator_arr)) :
  numerator += numerator_arr[i] * (lcm // denominator_arr[i])

n_d_gcd = GCD(numerator,lcm)
print(f"{numerator // n_d_gcd} {lcm // n_d_gcd}")