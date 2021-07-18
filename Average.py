

l=[10,20,30,40]

#l=[20,60,40]

def avg(l):
    sum=0
    for x in l:
        sum=sum+x
    n=len(l)
    return sum/n



def average(l):
    return sum(l)/len(l)

print(average(l))