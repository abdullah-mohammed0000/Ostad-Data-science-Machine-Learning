import functools
x = 10 # global variable
print(x)

def func():
    y = 19 #local variable
    x = 23
    print(x)
    print(y)

func()

print(x)
#print(y) #not printable as y is local variable


#LEGB Rule
# L: Local
# E: Enclosing function
# G: Global
# B: Built-in

n = "Global Variable"

def outer_func():
    
    n = "Enclosing Variable"
    
    def inner_func():
        nonlocal n #change enclosing variable not global variable
        #gloabal n #change global variable not enclosing variable
        n = "Local Variable"
        print(n)
    
    inner_func()
    print(n)

outer_func()
print(n)

