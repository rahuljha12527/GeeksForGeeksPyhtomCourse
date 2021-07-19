
# even=[10,30,80]

# odd [41,15]


def getEvenOdd(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    
    return even,odd

l=[10,41,30,15,80]
even,odd=getEvenOdd(l)
print(even)
print(odd)
