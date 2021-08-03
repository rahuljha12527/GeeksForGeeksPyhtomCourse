
from Collections import Counter

def isPalPer(s):
    cnt=Counter(s)
    odd=0
    for freq in cnt.values():
        if freq%2!=0:
            odd=odd+1
            if odd>1:
                return False
    return True




 
print(isPalPer("geeksforgeeks"))