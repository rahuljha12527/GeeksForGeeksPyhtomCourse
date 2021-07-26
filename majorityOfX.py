    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, n, x, y):
        # code here
        count=0
        counter=0
        for i in range(0,n):
            if x == arr[i]:
                count+=1;
        
        
        for j in range(0,n):
            if y==arr[j]:
                counter+=1;
    
        #print(count)
       # print(counter)
        
        if count > counter:
            return x
        if count<counter:
            return y
        if count==counter:
            if x<y:
                return x
            else:
                return y
            #return x
        #if count==counter or x>y:
         #   return y
    

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        x,y=map(int,input().strip().split())
        
        print(Solution().majorityWins(arr,n,x,y))
        T-=1

# } Driver Code Ends