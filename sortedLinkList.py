


def sortedLinkedList(head,x):
    temp=Node(key)

    if head==None:
        return temp
    

    if x<head.data:
        temp.next=head.next
        return temp

    
    else:

        curr=head
        while curr.next!=None and curr.next.data<x:
            curr=curr.next
        temp.next=curr.next
        curr.next=temp
        return head


