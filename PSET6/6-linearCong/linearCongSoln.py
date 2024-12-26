import math
def linearCong(m,b,N):
    # Your code here
    # The function should either "return None" or "return r,M", where the solution is x = r momod M.
    gcd = math.gcd(m, N)
    if(gcd == 1):
        return (b*pow(m, -1, N) % N, N)
    if(b % gcd != 0):
        return None
    M = N//gcd
    return ((b // gcd)*pow(m // gcd, -1, M)) % M, M