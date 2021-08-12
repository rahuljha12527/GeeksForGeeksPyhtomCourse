

def lastIndex(l,x):
    for i in reversed(range(len(l))):
        if l[i]==x:
            return i
    return -1