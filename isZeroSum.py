def isZeroSum(l):
    n=len(l)
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(l[i:j])==0:
                return True
    return False
