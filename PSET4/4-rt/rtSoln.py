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
def rt(a1,m1,a2,m2):
    # Your code here
    a = (a1+(a2-a1)*inv(m1, m2)*m1) % (m1*m2)
    return a
