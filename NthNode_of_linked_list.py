def getNthFromLast(head,n):
    #code here
    
    curr=head
    len=0
    while curr is not None:
        curr=curr.next
        len=len+1
    
    
    #print(len)
    find_ll=len-n
    #print(find_ll)
    if find_ll<0:
        return -1
    
    
    counter=0
    curr=head
    while curr is not None:
        
        if counter==find_ll:
            
            return curr.data
        #print(curr.data)
        counter=counter+1    
        curr=curr.next
    
    
    return -1
        