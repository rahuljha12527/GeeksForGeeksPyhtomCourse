from collections import OrderedDict
class Solution:
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        
        #using dictionary to store count of votes for each name.
        mp=OrderedDict({})
        
        #storing the frequency of names in the dictionary.
        for i in arr:
            mp[i]=mp.get(i,0)+1
        
        maxx=-1
        ans=""
        
        #sorting the dictionary by key or name which means names will 
        #be sorted in lexicographically smaller order.
        mp=OrderedDict(sorted(mp.items()))
        
        #iterating over the dictoinary to find the name with highest frequency.
        for key,value in mp.items():
            
            #updating answer whenever we get any name with frequency 
            #greater than frequency of name stored previously.
            if value>maxx:
                maxx=value
                answer=key
                
        #storing name with highest votes and the number of votes in a list.
        result = [answer,maxx]
        
        #returning the list.
        return result