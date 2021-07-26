class Get {
    public static void reverseArray(int arr[], int n) {
        // Your code here
        int []temp=new int[n];
        int j=0;
        for(int i=n-1;i>=0;i--){
            temp[j]=arr[i];
            j++;
        }
        
        
        for (int i=0;i<n;i++){
            arr[i]=temp[i];
        }
        
    }
}

// Rerverse array in python good way
def reverseArray(arr,n):
    
    for i in range(0,n//2):
        temp=arr[i]
        arr[i]=arr[n-i-1]
        arr[n-i-1]=temp


