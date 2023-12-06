N = int(input())
ans = list()
def recursion(s,l,r) :
    if l >= r : return [str(1),str(l + 1)]
    elif s[l] != s[r] : return [str(0),str(l + 1)]
    else : return recursion(s, l+1, r-1)

def isPalindrome(s) :
    return recursion(s, 0, len(s)-1)

for _ in range(N) :
  T = input()
  print(" ".join(isPalindrome(T)))