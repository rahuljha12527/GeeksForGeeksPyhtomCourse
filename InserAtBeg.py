
class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
    def insertBegin(head,key):
        temp=Node(key)
        temp.next=head
        return temp
    

    head=None
    head=insertBegin(head,10)
    head=insertBegin(head,20)
    head=insertBegin(head,30)
    printList(head)
    