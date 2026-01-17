a = 33
b =34
if b>a:
    print("b is greater than a")



f = 100
g = 200

if g>f:
    print("g is greater than f")
elif f==g:
    print("f is equal to g")
elif f<g:
    print("f is less than g")
else:
    print("None of the conditions are true")    


z = 50
l = 60
k = 70

if l>z and k>z:
    print("Both conditions are true")

if l>z or k<z:
    print("At least one of the conditions is true")


#Nested if statement

x = 10

if x>5:
    print("x is greater than 5")
    if (x>10):
        print("x is also greater than 10")
    else:
        print("x is not greater than 10")
else:
    print("x is not greater than 5")      


#Using pass statement in if-else

if a>b:
    pass      