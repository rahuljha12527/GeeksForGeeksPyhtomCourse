def sumOfElements(head):
    #code here
    sum_ans=0
    while head!=None:
        sum_ans=sum_ans+head.data
        head=head.next
    
    
    return sum_ans
    