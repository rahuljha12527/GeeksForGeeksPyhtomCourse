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



####################################################

s="geeksforgeeks"

l2=[x for x in s if x in "aeiou"]

print(l2)

l3=["geeks","ide","courses","gfg"]
l4=[x for x in l3 if x.startswith("g")]

l6=[x.upper() for x in l3 if x.startswith("g")]
print(l6)

print(l4)

l5=[x*2 for x in range(6)]
print(l5)



#################################################################################################

##   SET COMPREHENSION


l=[10,20,3,4,10,20,7,3]

s1={x for x in l if x%2==0}

s2={x for x in l if x%2!=0}

print(s1)

print(s2)








#####################################################################################################

## DictionaryComprehension


l1=[1,3,4,2,5]

d1={x:x**3 for x in l1}

print(d1)


d2={x:f"ID{x}" for x in range(5)}
print(d2)


r1=[101,103,102]
r2=["gfg","ide","courses"]

d3={r1[i]:r2[i] for i in range(len(r2))}
print(d3)