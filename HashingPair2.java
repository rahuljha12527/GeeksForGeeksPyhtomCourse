class Geeks
{
    //Complete this function
    //Function to check if two numbers in array have sum equal to the given sum.
    public static int sumExists(int arr[], int N, int sum)
    {
        
        //Your code here
        
        HashMap<Integer,Integer> map=new HashMap<Integer,Integer>();
        
        for(int i=0;i<N;i++){
             if(map.containsKey(arr[i])){
               map.put(arr[i],1+map.get(arr[i]));
           }
           else{
               map.put(arr[i],1);
           }
        }
        
        int counter=0;
        for(int i=0;i<N;i++){
           if(map.containsKey(sum-arr[i]) && arr[i]!=sum-arr[i]){
               counter++;
           }
       }
       
       if(counter>1){
           return 1;
       }
       else{
           return 0;
       }
       
     }
      
    
}
