def insertInHead(head,x):
    #code here
    
    temp=Node(x)
    if head==None:
        return temp
    
    
    curr=head.next
    while curr.next!=head:
        #print(curr.data)
        curr=curr.next
    
    
    
    curr.next=temp
    temp.next=head
    return temp