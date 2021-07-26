class Solution{
    public:
        int immediateSmaller(int arr[], int n, int x){
        int diff = INT_MAX;
        int ans = -1;
        
        for(int i =0; i<n; i++)
        {
            if((arr[i] < x) && (abs(arr[i]-x) < diff))
            {
                ans = arr[i];
                diff = abs(arr[i]-x);
            }
        }
    
        
        return ans;
        
    }
};


class Solution:
    def immediateSmaller(self,arr,n,x):
        ans=-1
        diff = 10000000
        for e in arr:
            if e<x and x-e < diff:
                ans=e
                diff = x-e
        return ans