mytuple = ("a","b","c","d","e","f","g","h","i","j","k")
print(mytuple)
print(len(mytuple))
print(mytuple[1])
print(mytuple[-1])
print(mytuple[2:4])



#Conversion to List

y = list(mytuple)
print(y)

y[1] = "Kiwi"
print(y)
mytuple = tuple(y)
print(mytuple)


#Unpacking a tuple
fruits = ("apple", "banana", "Cherry")
(green, yellow, red) = fruits  

print(green)
print(yellow)
print(red)

fruits1 = ("apple", "banana", "Cherry",1,2,3)

(f1,f2,f3,*num) = fruits1
print(f1)
print(num)

tuple1 = ("a","b","c")
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)

