a = [1,2,3,4,5,'a',6,7,8,9,10]

b = [i for i in a]
print(b)

C = [i for i in a if type(i) == int]
print(C)