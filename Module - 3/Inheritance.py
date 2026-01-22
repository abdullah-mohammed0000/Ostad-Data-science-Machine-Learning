#Father, Mother, Grandpa, Inno, Multi

#Single inheritance

class Father:
    def skills(self):
        print("I can code in C++")

class Son(Father):
    pass


inno = Son()
inno.skills()

#Hierarchical Inheritance
class Mom:
    def cooking(self, name):
        print(f"{name} is Cooking delicious biriyani")


class Inno(Mom):
    pass

class Multi(Mom):
    pass

inno = Inno()
multi = Multi()

inno.cooking("Inno")
multi.cooking("Multi")


#Multilevel

class Grandpa:
    def advice(self):
        print("Never ignore bugs!")

class Father(Grandpa):    
    def teach(self):
        print("Teaching Java")    

class Son(Father):
    pass    


inno = Son()
inno.advice()
inno.teach()

#Multiple Inheritance
class Mother:
    def discipline(self):
        print('Go to bed at 10 PM!')

class UncleLogic:
    def math(self):
        print("Solving equations....")   

class Daughter(Mother, UncleLogic):
    pass


multi = Daughter()
multi.discipline()
multi.math()


#Method Overloading

class ReportCard:
    def marks(self, math = None, english = None):
        if math is not None and english is not None:
            print(f"Math: {math}, English: {english}")
        elif math is not None:
            print(f"Math: {math}")  

        elif english is not None:
            print(f"English: {english}")
        else:
            print("No marks given")    


inno_report = ReportCard()
inno_report.marks()
inno_report.marks(90)
inno_report.marks(90,85)         


#Method Overriding

class Parent:
    def role(self):
        print("I am the boss!")

    def test(self):
        print("I am testing")    


class Child(Parent):
    def role(self):
        print("I run the show now!")

multi = Child()
multi.role()    
multi.test()  


#Encapsulation

class Family:
    def __init__(self):
      self.__secret_fund = 5000 #private

    def get_fund(self):
        return self.__secret_fund  
    

dad = Family()
print(dad.get_fund())    



#Poymorphism

class Role:
    def act(self):
        pass

class Cook(Role):
    def act(self):
        print("Cooking dinner")

class Doctor(Role):
    def act(self):
        print("Prescribing medicine...")


def daily_roles(role):
    role.act()


daily_roles(Cook())
daily_roles(Doctor())                    