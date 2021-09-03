class Solution:
    def stackMiddle(self,n,stack):
        #code here
        #print(4//2+1)
        
        if n%2==0:
             oper=n//2
             while oper>0:
                 stack.pop()
                 oper-=1
        else:
            oper=n//2+1
            while oper>1:
                stack.pop()
                oper-=1
        
        return stack.pop();
