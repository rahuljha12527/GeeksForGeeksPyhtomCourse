def joinTheLists(head1, head2):
    #code here
    
    if head1==None:
        
        return head2
    
    if head2==None:
        return head1
    
    
    
    
    
    
    curr=head1
    while curr.next is not None:
        curr=curr.next
    
    
    curr.next=head2
    return head1
    
    