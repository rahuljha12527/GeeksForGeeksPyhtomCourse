class Solution{
  public:
  
  
    int isRev(int n,int temp){
        
        if(n==0){
            return temp;
        }
        
        temp=(temp*10)+(n%10);
        
        return isRev(n/10,temp);
        
    }
    bool isPalin(int N)
    {
        //Your code here
        //You may use a helper function if you like
        
        int temp=isRev(N,0);
        
        if(temp==N){
            return true;
        }
        
        else{
            return false;
        }
    }
};