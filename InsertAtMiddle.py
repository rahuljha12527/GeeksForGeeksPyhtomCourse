def insertInMid(head,node):
    #code here
    
    if head==None:
        return node
    
    fast=head.next
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    
    
    node.next=slow.next
    slow.next=node
    
    
    return head