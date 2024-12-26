def extEuc(a, b):
    x1, y1 = 1, 0
    x2, y2 = 0, 1
    while(b!=0):
        x1c =x1
        y1c =y1
        x1, y1 = x2, y2
        x2, y2 = x1c - (a//b)*x2, y1c - (a//b)*y2
        a, b = b, a%b
    return x1, y1

def mFromPowers(N,e,f,me,mf):
    # Your code here
    u, v = extEuc(e, f)
    return (pow(me, u, N)*pow(mf, v, N)) % N