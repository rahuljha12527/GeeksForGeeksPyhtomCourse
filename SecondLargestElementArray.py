
l=[5,20,12,10,20,10,12]

def getMax(l):
    res=l[0]
    for i in range(1,len(l)):
        if res<l[i]:
            res=max(res,l[i])
    return res


def getSecondLargestElement(l):
    if len(l)<=1:
        return None
    
    lar=getMax(l)
    slar=None

    for x in l:
        if x!=lar:
            if slar==None:
                slar=x
            else:
                slar=max(slar,x)
    return slar

    


print(getSecondLargestElement(l))



