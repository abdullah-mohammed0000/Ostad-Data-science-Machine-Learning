a = [1,2,3,4,'a',5,6,7,8]
b = [2,3,4,5,'b',6,7,8]

for i in a:
    if type(i) == str:
        break
    else:
        print(i)

print("\n")        

for j in b:
    if type(j) == type('v'):
        break
    else:
        print(j)
print("\n") 
for k in a:
    if type(k) == str:
        continue
    else:
        print(k)        

print("\n") 
for m in b:
    if type(m) == type('v'):
        continue
    else:
        print(m)