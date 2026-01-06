import functools

def square(x):
 return x * x
print(square(5))

square = lambda x: x*x*x
print(square(4))

add = lambda a,b : a + b
print(add(1,2))

students = [('Rahim', 60), ('Karim', 50), ('Aalam', 70)]
sorted_students = sorted(students, key = lambda x: x[1])
print(sorted_students)

nums = [1,2,3,4]

sq_nums = list(map(lambda x: x*x == 0, nums))
print(sq_nums)

even = list(filter(lambda x: x%2 == 0, nums))
print(even)

sum = functools.reduce(lambda x, y: x + y, nums)
print(sum)
