class Solution
{
    // Complete the function
    public static int immediateSmaller(int arr[], int n, int x)
    {
        // Your code here
        int smaller=-1;
        for(int i=0;i<n;i++){
            
            if(arr[i]>smaller && arr[i]<x){
                smaller=arr[i];
            }
        }
        
        return smaller;
    }
}