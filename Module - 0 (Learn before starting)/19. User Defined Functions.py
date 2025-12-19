#no input no return
def greet():
    print("Hello, welcome to Ostad")

greet();

#with input no return
def greet_user(name):
    print(f"Hello, {name}, welcome to Ostad")

greet_user("Alice");

#with input with return
def add(a, b):
    return a + b
result = add(5, 7)
print(f"The sum is: {result}")

#no input with return
def get_favorite_language():
    return "Python"
language = get_favorite_language()
print(f"My favorite programming language is: {language}")
  