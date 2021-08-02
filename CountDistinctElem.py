def cDistrict(l):
    res=1
    for i in range(1,len(l)):
        if l[i] not in l[0:i]:
            res=res+1
    return res



def cDis(l):
    s=set(l)
    return len(s)

l=[10,20,10,30,30,20]
print(cDistrict(l))

print(cDis(l))

 