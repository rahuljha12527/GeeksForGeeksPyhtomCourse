def isCircular(head):
    # Code here
    
    if head==None or head.next==None:
        return 0
    elif head.next==head:
        return 1
    
    else:
        
        curr=head
        while curr.next!=None and curr.next!=head:
            curr=curr.next
        
        if curr.next==None:
            return 0
        elif curr.next==head:
            return 1
            
            
            
        
        