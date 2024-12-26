def eucAlg(a, b):
    while(b!=0):
        a, b = b, a%b
    return a

def numCoprimePairs(A,B):
    num = 0
    for i in range (A, B+1):
        for j in range(A, B+1):
            if eucAlg(i, j) == 1:
                num+=1
    return num