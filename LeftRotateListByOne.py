

l=[10,20,30,40]

l=l[1:]+l[0:1]

print(l)


l=[10,20,30,40]

l.append(l.pop(0))

print(l)

l=[10,20,30,40]
def rotateByOne(l):
    n=len(l)
    x=l[0]
    for i in range(1,len(l)):
        l[i-1]=l[i]
    l[n-1]=x
    return l


rotateByOne(l)
print(l)