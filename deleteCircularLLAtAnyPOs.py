def delHead(head):
    
    if head==None or head.next==None:
        return head
    
    else:
        curr=head
        while curr.next!=head:
            curr=curr.next
        curr.next=head.next
        return curr.next
        
def deleteAtPosition(head,pos):
    #code here
    
    if head==None or head.next==None:
        return head
    
    
    elif pos==1:
        return delHead(head)
    
    
    else:
        curr=head
        for i in range(pos-2):
            curr=curr.next
        
        curr.next=curr.next.next
        return head
            