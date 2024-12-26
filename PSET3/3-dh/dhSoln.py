import random
def inv(a, b):
    x1, y1 = 1, 0
    x2, y2 = 0, 1
    while(b!=0):
        x1c =x1
        y1c =y1
        x1, y1 = x2, y2
        x2, y2 = x1c - (a//b)*x2, y1c - (a//b)*y2
        a, b = b, a%b
    return x1

def modpow(a,n,m):
    prod = 1
    if n < 0:
        a = inv(a, m)
        n *= -1
    while n > 0:
        if n % 2 == 1:
            prod = (prod * a) % m
            n = n - 1
        n = n//2
        a = (a**2) % m
    return prod

def dh(g,p,B):
    a = random.randint(1, p-1)
    A = modpow(g, a, p)
    S = modpow(B, a, p)
    return A,S,
