

def findOdd(l):
    res=None
    for x in l:
        count=l.count(x)
        if(count%2!=0):
            res=x
            break
    return res



def findOddWithXor(l):
    res=0
    for x in l:
        res=res^x
    return res




l=[10,20,20,30,10]
print(findOdd(l))

print(findOddWithXor(l))