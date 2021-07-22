
l=[5,20,12,10,20,10,12]

##############################################################

### Naive Solution
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


#########################################################################################

 ########### Efficient Solution


def getSecLargest(l):
     
     if len(l)<=1:
         return None
     lar=l[0]
     slar=None

     for x in l[1:]:
         if x > lar:
             slar=lar
             lar=x
         elif x!=lar:
             if slar==None or slar<x:
                 slar=x
     return slar













print(getSecLargest(l))     



