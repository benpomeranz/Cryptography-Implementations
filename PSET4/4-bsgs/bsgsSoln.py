import math

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

def bsgs(g,h,p):
    # your code here
    n = math.ceil(math.sqrt(p-1))
    babyList = {}
    giantList = []
    gnegn = modpow(g, -n, p)
    currbabe = 1
    currbig = h
    for i in range(0, n):
        babyList[currbabe] = i
        currbabe = currbabe*g % p
        giantList.append(currbig)
        currbig = currbig*gnegn % p
    for i in range(0, n):
        if giantList[i] in babyList:
            return babyList[giantList[i]]+n*i
