class Avenger:
    def fight(self):
        print("Avenger is fighting!")


ironman = Avenger()
ironman.fight()


hulk = Avenger()
hulk.fight()


#Introducing method
class Avenger:
    def introduce(self, name):
        print(f"I am {name}, and I protect the world!")

ironman = Avenger()
ironman.introduce("Iron man")       


hulk = Avenger()
hulk.introduce("Hulk")


#Default Constructor
class Avenger1:
    def __init__(self):
        self.name = "Abdullah"
    
    def introduce1(self, skill):
        print(f"I am {self.name}, and I Know {skill}!")

captain = Avenger1()   
captain.introduce1("DS & ML")   


#Parameterized constructor

class Avenger2:
     def __init__(self, name, power):
        self.name = name
        self.powerful = power
    
     def show(self):
        print(f"I am {self.name}, and I Know {self.powerful}!")

captain1 = Avenger2("Abdullah", "DS & ML")   
captain1.show()


#Inheritance

class Hero:
    def protect(self):
        print("Protecting the Earth!")

class Ironman(Hero):
  def fly(self):
      print("Flying in the suit")

tony = Ironman()
tony.protect() #inherited
tony.fly()  #own method  