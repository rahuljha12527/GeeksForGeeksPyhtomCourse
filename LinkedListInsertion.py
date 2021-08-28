class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        # code here
        
        temp=Node(x)
        temp.next=head
        return temp
        
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here
        
        temp=Node(x)
        if head==None:
            head=Node(x)
            return head
        
        if head.next==None:
            head.next=temp
            return head
         
        
        
        curr=head
        while curr.next!=None:
            
            curr=curr.next
            #print(curr.next.data)
        #print(curr.data)
        curr.next=temp
        
        
        return head
