################### Merge Two sorted array

def MergeLists(a,b):

    res=[]
    m=len(a)
    n=len(b)
    i=0
    j=0

    while i<m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i=i+1
        else:
            res.append(b[j])
            j=j+1
    

    while i<m:
        res.append(a[i])
        i=i+1
    while j<n:
        res.append(b[j])
        j=j+1

    return res    

