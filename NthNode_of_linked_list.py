def getNthFromLast(head,n):
    #code here
    
    curr=head
    len=0
    while curr is not None:
        curr=curr.next
        len=len+1
    
    
    #print(len)
    find_ll=len-n
    #print(find_ll)
    if find_ll<0:
        return -1
    
    
    counter=0
    curr=head
    while curr is not None:
        
        if counter==find_ll:
            
            return curr.data
        #print(curr.data)
        counter=counter+1    
        curr=curr.next
    
    
    return -1
    
    ##################### geeksgeeksforgeeks approach

    def getNthFromLast(head,n):
    
    #using two pointers, similar to finding middle element.
    curr_node = head
    nth_node = head

    #traversing first n elements with first pointer.
    while n :
        if n and curr_node == None:
            return -1
        curr_node = curr_node.next
        n-=1

    #now traversing with both pointers and when first pointer gives null 
    #we have got the nth node from end in second pointer since the first 
    #pointer had already traversed n nodes and thus had difference of n 
    #nodes with second pointer.
    while curr_node :
        curr_node = curr_node.next
        nth_node = nth_node.next

    #returning the data of nth node from end.
    return nth_node.data
        