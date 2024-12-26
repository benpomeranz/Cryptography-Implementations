import math
def linearCong(m,b,N):
    gcd = math.gcd(m, N)
    if(gcd == 1):
        return (b*pow(m, -1, N) % N, N)
    if(b % gcd != 0):
        return None
    M = N//gcd
    return ((b // gcd)*pow(m // gcd, -1, M)) % M, M

def extractKey(p,g,A,d1,s11,s12,d2,s21,s22):
    # Your code here
    k, m = linearCong(s12-s22, d1-d2, p-1)
    while not((pow(g, k, p) == s11)):
        k += m
    a, m = linearCong(s11, (s12*k-d1)*-1, p-1)
    while not((pow(g, a, p) == A)):
        a += m
    return a