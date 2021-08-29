



def insertInTail(head,x):
    #code here
    temp=Node(x)
    if head==None:
        return temp
    
    
    
    else:
        curr=head.next
        while curr.next!=head:
            curr=curr.next
        
        
        curr.next=temp
        temp.next=head
        return head
        