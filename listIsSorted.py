

l=[10,20,40,50,30]


def listIsSoretd(l):

    for i in range(1,len(l)):
        if l[i-1]>l[i]:
            return False
    


    return True





if(listIsSoretd(l)==True):
    print("It is sorted")
else:
    print("It is not sorted")




print(listIsSoretd(l))