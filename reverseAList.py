
############################################################

#################### reverse a list

l=[10,20,30]
l.reverse()
print(l)


##################################################################


############################# reverse a new list

l=[10,20,30]
now_l=list(reversed(l))
print(now_l)

##################################################### reverse and return new list

new_l=l[::-1]
print(new_l)


def reverselist(l):
    start=0
    end=len(l)-1
    while start<end:
        l[start],l[end]=l[end],l[start]
        start=start+1
        end=end-1
    return l



P=[10,20,30,40,50]

reverselist(P)
print(P)