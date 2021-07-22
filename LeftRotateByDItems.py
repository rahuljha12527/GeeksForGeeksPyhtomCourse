

#########################################

########### Using Direct Method

l=[10,20,30,40,50]
d=2
l=l[d:]+l[:d]
print(l)


###########################################################

###################### Another Mehtod

## TimeComplecty O(n)

## Auxilary Space O(1)



l=[10,20,30,40,50]
def leftRotate(l,d):
    for i in range(0,d):
        l.append(l.pop(0))


d=2
leftRotate(l,d)
print(l)







####################################################################

######## Time Complexity o(n) and space complexity O(1)

l=[10,20,30,40,50]
d=2
def leftRotates(l,d):

    n=len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)



def reverse(l,a,b):

    while a<b:

        l[a],l[b]=l[b],l[a]
        a=a+1
        b=b-1
    return l





leftRotates(l,d)
print(l)