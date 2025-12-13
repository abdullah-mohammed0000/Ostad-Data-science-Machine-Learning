user_input = input(("Enter your name: "))

a = "My name is {}".format(user_input)
print(a)

#Long version

a = 'Abdullah'
b = 'Mohammed'
age = 25

print("My name is {a} {b} and I am {age} years old.".format(b=b, a=a, age=age))


#short version (f-string)
c = f"My name is {a} {b} and I am {age} years old."
print(c)