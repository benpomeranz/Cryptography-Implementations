def ecAdd(P, Q, A, p):
    # Your code here
    # Should either return 0 (for point at infinity)
    #   or return (x,y), where x,y are in Z / p Z
    # Currently assume points P,Q, lie on elliptic curve eAB 
    if [P, Q] == [0, 0]:
        return 0
    if P == 0:
        return Q
    if Q == 0:
        return P
    if P == Q:  # tangent
        if P[1] == 0:  # tangent at 0
            return 0
        slope = (3 * P[0] ** 2 + A) * pow(2 * P[1], -1, p)
    else:
        if P[0] == Q[0]:
            return 0
        slope = (P[1] - Q[1]) * pow(P[0] - Q[0], -1, p)
    x = (slope ** 2 - P[0] - Q[0]) % p
    y = (slope * (x - P[0]) + P[1]) % p
    return (x, (p - y) % p)

def ecMult(n,P,A,B,p):
    # Your code here
    if n<0:
        n = n*-1
        P = (P[0], -1*P[1])
    prod = 0
    if P == 0:
        return 0
    if P[1] < 0:
        P = (P[0], p - P[1])
    while n > 0:
        if n % 2 == 1:
            prod = ecAdd(prod, P, A, p)
            n = n - 1
        n = n//2
        P = ecAdd(P, P, A, p)
    return prod
