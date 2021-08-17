def search(self,arr, N, X):
        #Your code here
        
        for i in range(0,N):
            
            if arr[i]==X:
                
                return i
        
        return -1
        