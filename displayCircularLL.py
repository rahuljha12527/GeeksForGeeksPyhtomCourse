
def displayList(head):
    #code here
    
    dis_List=[]
    if head==None:
        return None
    
    
    else:
        #print("head")
        
        dis_List.append(head.data)
        curr=head.next
        while curr!=head:
            #print(curr.data)
            dis_List.append(curr.data)
            #print(curr.data,endl=" ")
            curr=curr.next
        
        
        return dis_List