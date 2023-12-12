import sys

input = sys.stdin.readline

N = int(input())

def add_star(n) :
    if n == 1 : return '*'

    star = add_star(n // 3)
    stars = list()

    for s in star :
        stars.append(s*3)
    
    for s in star :
        stars.append(f"{s}{' ' * (n//3)}{s}")
    
    for s in star :
        stars.append(s*3)
    
    return stars

print("\n".join(add_star(N)))