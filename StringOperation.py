

s1="geeksforgeeks"
s2="geeks"
print(s2 in s1)
print(s2 not in s1)


print(s1.index(s2))
print(s1.rindex(s2))
print(s1.index(s2,0,13))


s="--geeksforgeeks---"
print(s.strip("-"))
print(s.lstrip("-"))
print(s.rstrip("-"))

########################################### find method


s1="geeks for geeks"
s2="geeks"
print(s1.find(s2))

print(s1.find("gfg"))
n=len(s1)
print(s1.find(s2,1,n))