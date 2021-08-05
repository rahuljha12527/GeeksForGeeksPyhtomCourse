class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        
        #using hash table to store count of each character.
        occurences=[0 for i in range(256)]
        
        #iterating over the string.
        for char in s:
            occurences[ord(char)]+=1
        
        for i in range(len(s)):
            #if count of current character is 1, we return it. 
            if(occurences[ord(s[i])]==1):
                return s[i]
                
        #if there is no non-repeating character then we return '$'.
        return '$'
    