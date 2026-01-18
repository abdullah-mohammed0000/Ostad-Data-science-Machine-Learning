Snacks = ["Chips", "Soda", "Cake"]
print("Snacks: ",Snacks)

#Adding into the List

Snacks.append("Biscuits")
print("Snacks: ",Snacks)


#Removing from the List
Snacks.remove("Soda")
print("Snacks: ",Snacks)

#List item in Alphabetical order
Snacks.sort()
print("Snacks: ",Snacks)

Snacks1 = ["Chips", "Cake", "Soda", "Pizza"]

print("First Snacks: ",Snacks1[0])
print(len(Snacks1))
print("Last Snacks: ",Snacks1[-1])

Snacks1[0] = "Juice"
print("Snacks: ",Snacks1)

#Position wise item inserting
Snacks1.insert(1, "Cookies")
print("Snacks: ",Snacks1)

#position wise item deleting

del Snacks1[3]
print("Snacks: ",Snacks1)

Last_Snacks1 = Snacks1.pop()
print("Removing Item: ",Last_Snacks1)
print("Snacks: ",Snacks1)

#Nested List

Party_Bags = [
["Chips", "Cookies"],
["Cake", "MOJO"],
["Pizza", "Pasta"]

]


for bag in Party_Bags:
   
    print(bag)
    for item in bag:
       print("Bag has: ",item)

print('\n')
print('\n')
print('\n')
print('\n')

for index, bag in enumerate(Party_Bags):
    print(f"Bag {index} : ", bag)
    print(bag)
    for item1 in bag:
       print("Bag has: ",item1)



