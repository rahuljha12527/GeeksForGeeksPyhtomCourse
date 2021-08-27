def displayList(head):
    #code here
    
    l=[]
    while head!=None:
        l.append(head.data)
        head=head.next
    return l
    