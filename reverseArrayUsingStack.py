class Solution:
    def reverseArray(self,n,arr):
        #code here
        stack=[]
        # for i in range(0,n):
        #     #print(arr[i])
        #     stack.append(arr[i])
        # return stack
        k=n
        while n>0:
            stack.append(arr[n-1])
            n-=1
        
        #return stack
        i=k-1
        while stack:
            arr[i]=stack.pop()
            i-=1
        
        return arr;