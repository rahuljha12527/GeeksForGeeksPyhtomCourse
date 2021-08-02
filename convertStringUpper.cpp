class Solution{
  public:
    string caseConversion(string str){
    
        for(int i = 0;i<str.size();i++){
            if(str[i] >= 97 && str[i] <= 122){
                str[i] = (char)str[i]-32;
            }
        }
        
        return str;
        
    }
};