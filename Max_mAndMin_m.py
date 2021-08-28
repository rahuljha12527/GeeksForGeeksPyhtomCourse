def maximum(head):
    #code here
    
    curr=head
    max_m=head.data
    while curr:
        if curr.data>max_m:
            max_m=curr.data
        curr=curr.next
    return max_m
    
def minimum(head):
    #code here
    
    min_m=head.data
    curr=head
    while curr:
        if curr.data<min_m:
            min_m=curr.data
        curr=curr.next
    return min_m