class Solution:
    def countO(self,arr,low,high): 
          
        if high>=low: 
              
            # get the middle index 
            mid = int(low + (high-low)/2)
              
            # check if the element at middle index is last 1 
            if ((mid == high or arr[mid+1]==0) and (arr[mid]==1)): 
                return mid+1
                  
            # If element is not last 1, recur for right side 
            if arr[mid]==1: 
                return self.countO(arr, (mid+1), high) 
                  
            # else recur for left side 
            return self.countO(arr, low, mid-1) 
          
        return 0
        
    def countOnes(self,A,N):
        return self.countO(A,0,len(A)-1









################################# my soluton


#User function Template for python3

class Solution:
    ##Complete this code
    
    def firstOccurence(self,arr,N,K):
        
        low=0
        high=N-1
        
        while low<=high:
            
            
            mid=(low+high)//2
            
            #print(arr[mid])
            if arr[mid]<K:
                low=mid+1
            elif arr[mid]>K:
                high=mid-1
            else:
                
                if mid==0 or arr[mid]!=arr[mid-1]:
                    #print("end",mid)
                    return mid
                else:
                    high=mid-1
        return -1
            
       
    
    def lastOccurence(self,arr,N,K):
        
        low=0
        high=N-1
        
        
            
            
        while low<=high:
            
                
            mid=(low+high)//2
            #print(arr[mid])    
                
            if arr[mid]<K:
                low=mid+1
            elif arr[mid]>K:
                high=mid-1
            else:
                #print("mid",mid)
                if mid==len(arr)-1  or arr[mid]!=arr[mid+1]:
                    #print("end3",mid)
                    return mid
                    
                else:
                    low=mid+1
        return -1
                    
                
                
            
    def countOnes(self,arr, N):
        #Your code here
        arr.sort()
        OneOccurence=self.firstOccurence(arr,N,1)
        
        if OneOccurence==-1:
            return 0
        
        OneLastOccurence=self.lastOccurence(arr,N,1)
        
        #print(OneOccurence)
        #print(OneLastOccurence)
        
        
        return OneLastOccurence-OneOccurence+1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            ob=Solution()
            print(ob.countOnes(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends