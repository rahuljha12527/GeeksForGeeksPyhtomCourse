class Solution
{
    //Function to find the first non-repeating character in a string.
    static char nonrepeatingCharacter(String S)
    {
        //Your code here
        
        HashMap<Character,Integer> map=new HashMap<Character,Integer>();
        
        
        char ans='\0';
        //char subAns='-1';
        //String answer='\-1';
        
        //char subAns=answer.charAt(0);
        
        for(int i=0;i<S.length();i++){
            if(map.containsKey(S.charAt(i))){
                map.put(S.charAt(i),1+map.get(S.charAt(i)));
            }
            
            else{
                map.put(S.charAt(i),1);
            }
            
            
        }
        
        for(int i=0;i<S.length();i++){
            if(map.get(S.charAt(i))==1){
                ans=S.charAt(i);
                return ans;
            }
        }
        
        return '$';
    }
}
