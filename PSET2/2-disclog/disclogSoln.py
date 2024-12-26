def disclog(g,h,p):
    if(h==1):
        return 0
    i = 1
    curr_g = g
    while(1):
        if curr_g == h:
            return i
        curr_g = (curr_g*g) % p
        i+=1
