class Geeks
{
    //Complete this function
    //Function to check if there is a pair with the given sum in the array.
    public static int sumExists(int arr[], int N, int sum)
    {
       //Your code here, Geeks
       HashMap<Integer,Integer>  map=new HashMap<Integer,Integer>();
       
       
       for(int i=0;i<N;i++){
           if(map.containsKey(arr[i])){
               map.put(arr[i],1+map.get(arr[i]));
           }
           else{
               map.put(arr[i],1);
           }
       }
       
       
       for(int i=0;i<N;i++){
           if(map.containsKey(sum-arr[i]) && arr[i]!=sum-arr[i]){
               return 1;
           }
       }
       
       
       return 0;
       
        
    }
}
