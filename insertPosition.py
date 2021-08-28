def insertAtPosition(head,pos,data):
    #code here
    
    temp=Node(data)
    if pos==0:
        #print(temp)
        tempp=Node(data)
        tempp.next=head
        #print(temp)
        return tempp
    
    
    len=0
    curr=head
    while curr:
        curr=curr.next
        len=len+1
    
    
    if pos>len:
        return head
    
    
    curr=head
    for i in range(pos-1):
        curr=curr.next
    
    
    temp.next=curr.next
    curr.next=temp
    
    return head


    def insertAtPosition(head,pos,data):

    node=Node(data)
    i=1
    while head and i<pos:
        i+=1
        head=head.next
    if head:
        node.next=head.next
        head.next=node