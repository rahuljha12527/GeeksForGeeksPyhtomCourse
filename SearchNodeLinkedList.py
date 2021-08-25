

def Search(head,x):
    pos=1
    curr=head

    while curr!=None:
        if curr.key==x:
            return pos
        
        pos=pos+1
        curr=curr.next
    return -1