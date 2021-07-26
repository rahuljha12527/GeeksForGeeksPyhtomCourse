def maximumElement(arr,n,):
    #return required result
    arr.sort()
    return arr[n-1]
    #code here



def minimumElement(arr,n):
    #return required result
    arr.sort()
    return arr[0]
    #code here


######################################################### Alternative way 
def maximumElement(arr,n,):
    #return required result
    maxm=-inf
    ans=-1
    for i in arr:
        if maxm < i:
            maxm=i
            ans=i
    return ans
        
        
      
    #code here



def minimumElement(arr,n):
    #return required result
    
    minm=inf
    ans=-1
    for i in arr:
        if minm > i:
            minm=i
            ans=i
    return ans
        