def ecdsaVerify(V,d,s1,s2):
    # Your code here
    # Either return True or return False
    G = (int("0xaa87ca22be8b05378eb1c71ef320ad746e1d3b628ba79b9859f741e082542a385502f25dbf55296c3a545e3872760ab7", 0), int("0x3617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7e819d7a431d7c90ea0e5f", 0))
    n = 39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956308152294913554433653942643
    p = 39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266088258938001861606973112319
    A = -3
    B = int("0xb3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aef", 0)
    v1 = d*pow(s2, -1, n) % n
    v2 = s1*pow(s2, -1, n) % n
    t_1 = ecMult(v1, G, A, B, p)
    t_2 = ecMult(v2, V, A, B, p)
    return ecAdd(t_1, t_2, A, p)[0] % n == s1 
    

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