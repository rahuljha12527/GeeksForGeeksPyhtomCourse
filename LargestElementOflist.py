
l=[10,20,5,50]

def getMax(l):
    for x in l:
        for y in l:
            if y>x:
                break;
        else:
            return x
    return None;


def getMaximum(l):
    if not l:
        return None
    else:
        res=l[0]
        for i in range(1,len(l)):
            if l[i] > res:
                res=l[i]
        return res;



print(getMax(l))

print(getMaximum(l));