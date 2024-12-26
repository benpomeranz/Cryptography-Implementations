import math

def isPrime(n):
    if n % 2 == 0:
        return False
    q = n-1
    k = 0
    while(q % 2 == 0):
        q = q//2
        k+=1
    for a in range(2, min(n-1, 100)):
        if(math.gcd(a, n)!= 1):
            return False
        aq = pow(a, q, n)
        anq = [aq]
        base = aq
        for i in range(1, k):
            base = pow(base, 2, n)
            anq = anq + [base]
        if (aq != 1) and (n-1 not in anq):
            return False
    return True

checkList = lambda ls : tuple(map(isPrime,ls))
