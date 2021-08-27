


def reverseLinkedList(head):
    stack=[]
    curr=head
    while curr is not None:
        stack.append(curr.key)
        curr=curr.next
    curr=head
    while curr is not None:
        curr.key=stack.pop()
        curr=curr.next
    return head


def reverseLinkedList(head):
    curr=head
    prev=None
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

    