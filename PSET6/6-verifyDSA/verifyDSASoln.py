def verifyDSA(p,q,g,A,d,s1,s2):
    # Your code here
    # Should return True or return False
    v1 = d*pow(s2, -1, q)
    v2 = s1*pow(s2, -1, q)
    return (s1 % q == (pow(g, v1, p)*pow(A, v2, p) % p) %  q)
