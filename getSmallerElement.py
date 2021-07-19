
#Input
# l=[8,100,20,40,3,7]


# x=10

#Output

# [8,3,7]



def getSmallerElement(l,x):
    smaller=[]
    for i in l:
        if i<x:
            smaller.append(i)
    

    return smaller;
        



l=[8,100,20,40,3,7]
x=10

print(getSmallerElement(l,x))