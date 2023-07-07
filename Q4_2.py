def list(l):
    lp = []
    for e in l:
        if e >= 0:
            lp.append(e)
    return lp

print(list([1,3,-5,-2,5,6,7]))