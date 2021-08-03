class Solution
{
    //Function to return non-repeated elements in the array.
    static ArrayList<Integer> printNonRepeated(int arr[], int n)
    {
        // add your code here
        
        HashMap<Integer,Integer> map=new HashMap<>();
        
        ArrayList<Integer> non_repeated=new ArrayList<>();
        
        
        for(int i=0;i<arr.length;i++){
            if(map.containsKey(arr[i])){
                map.put(arr[i],1+map.get(arr[i]));
            }
            
            else{
                map.put(arr[i],1);
            }
        }
        
        for(int i=0;i<arr.length;i++){
            if(map.get(arr[i])==1){
                non_repeated.add(arr[i]);
            }
        }
        
        return non_repeated;
    }
}