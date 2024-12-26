import random

def dsaBlind(p,q,g,A):
    # Your code here
    i = random.randint(1, q-1)
    j = random.randint(1, q-1)
    s1 = pow(g, i, p) * pow(A, j, p) % p % q
    d = s1*i*pow(j, -1, q) % q
    s2 = s1*pow(j, -1, q) % q
    return d,s1,s2
