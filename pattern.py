
################## Pattern searching


txt=input("Enter a text")
pat=input("Enter learn")

pos=txt.find(pat)
while pos>=0:
    print(pos)
    pos=txt.find(pat,pos+1)