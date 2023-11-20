import sys

N = int(sys.stdin.readline()) # 몇 개의 자연수를 입력 받을지에 대한 자연수
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)] # 리스트 선언 후 한 줄에 자연 수 두 개를 하나의 배열로 리스트 안에 넣는다.
ans = [] # 정답을 담을 리스트 선언
def GCD(a,b) :
  while b > 0:
    a, b = b, a % b
  return a

def LCM(a,b,gcd) :
  return (a * b) // gcd
  
for nm in arr :
  max_nm = max(nm)
  min_nm = min(nm)
  
  if min_nm == 1 :
    ans.append(max_nm)
  else :
    gcd = GCD(max_nm,min_nm)
    lcm = LCM(max_nm,min_nm,gcd)
    ans.append(lcm)
  
print("\n".join(list(map(str,ans))))