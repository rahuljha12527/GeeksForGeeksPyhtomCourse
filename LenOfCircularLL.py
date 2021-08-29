def getLength(head):
    #code here
    
    if head==None:
        return 0
        
    
    curr=head.next
    count=1
    while curr!=head:
        curr=curr.next
        count=count+1
    
    
    return count