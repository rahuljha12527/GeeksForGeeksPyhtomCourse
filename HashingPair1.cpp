int sumExists(int arr[], int N, int sum)
{
   //Your code here.
   int ans=0;
   for(int i=0;i<N;i++){
       for(int j=0;j<N;j++){
          if(arr[i]!=arr[j]){
            ans =arr[i]+arr[j];
          if(ans==sum){
              return 1;
          }     
          } 
         
           
       }
   }
       
       return 0;
   
}


//We have hashed x. Now x+y=sum can be rewritten as x=sum-y. 
//So, now we just need to traverse the array and see if the hash contains sum-arr[i]. If exists then the pair exists.