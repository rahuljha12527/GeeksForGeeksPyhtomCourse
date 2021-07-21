#Comprehension in  python

l1=[x for x in range(11) if x%2==0]

print(l1)

l2=[x for x in range(11) if x%2!=0]

print(l2)



#Get Smaller than x

def getSmaller(l,x):
    return [e for e in l if e<x]



l=[9,15,12,3,7,11]
x=10
print(getSmaller(l,x))




#Even list odd list

def getEvenOdd(l):
    even= [e for e in l if e%2==0]
    odd=[e for e in l if e%2!=0]

    return even,odd


even,odd=getEvenOdd(l)
print(even)
print(odd)