
def Reverse(self,N,k):
        
        if N==0:
            return k
        
        k=(k*10) + (N%10)
        
        return self.Reverse(N//10,k)
    def isPalin(self,N):
        #code here
        
        
        rev=self.Reverse(N,0);
        
        if rev==N:
            return 1
        else:
            return 0
            