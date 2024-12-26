import math
def isPrime(n):
    if n % 2 == 0:
        return False
    q = n-1
    k = 0
    while(q % 2 == 0):
        q = q//2
        k+=1
    for a in range(2, 50):
        if(math.gcd(a, n)!= 1):
            continue
        aq = pow(a, q, n)
        anq = [pow(a, (2**i)*q, n) for i in range(k)]
        if (aq != 1) and (n-1 not in anq):
            return False
    return True

def makeQP(qbits,pbits):
    # Your code here
    for i in range(2**(qbits-1), 2**qbits):
        if isPrime(i):
            q = i
            break
    nq = q * (((2**(pbits-1))//q)+1)
    if(nq % 2 == 1):
        nq += q
    while(nq<2**pbits):
        if isPrime(nq+1):
            p = nq+1
            break
        nq += 2*q
    return q,p

# This function can be used to test whether your function is working.
# You can use this function as-is to make sure you have the right bit lengths.
# Once you provide an ``isPrime'' function, uncomment the last 8 lines, which will check that your output is prime.
def checkQP(q,p,qbits,pbits):
    if q.bit_length() == qbits:
        print('q has the correct number of bits.')
    else:
        print('q is %d bits long, but should be %d bits long'%(q.bit_length(),qbits))

    if p.bit_length() == pbits:
        print('p has the correct number of bits.')
    else:
        print('p is %d bits long, but should be %d bits long'%(p.bit_length(),pbits))

    if p%q == 1:
        print('p is 1 mod q, as desired.')
    else:
        print('p is not 1 mod q.')

    if isPrime(q):
       print('q is prime.')
    else:
       print('q is not prime.')
    if isPrime(p):
       print('p is prime.')
    else:
       print('p is not prime.')
