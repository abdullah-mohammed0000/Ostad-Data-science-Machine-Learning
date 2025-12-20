def my_func(f_name, l_name, age):
    print(f"My name is {f_name} {l_name} and I am {age} years old.")

my_func(l_name="khan", f_name="Rahim", age=25)    


#Arbitary Number of Key word arguments

def my_func2(**kwargs):
    print(kwargs)
    print(f"My name is {kwargs['f_name']} {kwargs['l_name']} and I am {kwargs['age']} years old.")  

my_func2(l_name="khan", f_name="Rahim", age=25, city="Karachi")    