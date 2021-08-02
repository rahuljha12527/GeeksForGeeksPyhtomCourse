s1={10,20,30}

print(s1)

s2=set([20,30,40])

print(s2)

s3={}

print(type(s3))

s4=set()

print(type(s4))


print(s4)

s={10,20}

s.add(30)

print(s)

s.add(30)

print(s)

s.update([40,50])

print(s)

s.update([60,70],[80,90])

print(s)


s7={2,4,6,8}
s8={3,6,9}
print(s7 | s8)

print(s7 & s8)

print(s7-s8)

s={10,20,30,40,50}
print(len(s))

print(20 in s)
print(50 in s)
