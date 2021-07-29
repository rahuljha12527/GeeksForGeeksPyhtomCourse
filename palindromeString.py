

str=input("Enter a text")
s=0
l=len(str)-1

while s<l:
    if str[s]!=str[l]:
        print("No")
        break
    s+=1
    l-=1
    
    
else:
    print("Yes") 







############################################

str=input("Enter a string")
if s==s[::-1]:
    print("Yes")
else:
    print("No")

    