import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
C = []

def GCD(a,b) :
    if a % b == 0 :
        return b
    else :
        return GCD(b,a%b)

for i in range(len(arr) -1) :
    C.append(arr[i + 1] - arr[i])
    
for j in range(len(C)) :
    if j == 0 :
        gcd = GCD(C[j+1],C[j])
    else:
        gcd = GCD(C[j],gcd)
        
print(((arr[-1] - arr[0]) // gcd) - N + 1)