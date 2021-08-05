int sumExists(int arr[], int N, int sum)
{
    //Your code here
    int ans=0,counter=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(arr[i]!=arr[j]){
                ans=arr[i]+arr[j];
                //cout<<arr[i];
                if(ans==sum){
                    counter++;
                }
            }
        }
    }
    
    
    if(counter>1){
        return 1;
    }
    else{
        return 0;
    }
}