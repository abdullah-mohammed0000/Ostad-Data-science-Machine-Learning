thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple",1,2,True}
print(thisset)


#Adding
thisset.add("orange")
print(thisset)

#updating

thisset = {"a","banana", "cherry"}
tropical = {"pine", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["Kiwi", "Orange"]
thisset.update(mylist)
print(thisset)


#Removing
thisset.remove("banana")
print(thisset)

thisset.discard("Kiwi")
print(thisset)

x = thisset.pop()
print(x)
print(thisset)

x = thisset.pop()
print(x)
print(thisset)

#Clear

MissSet = {"Gayle",1,2,3,5,"Hayden"}
print(MissSet)
MissSet.clear()
print(MissSet)


#Union, Intersection, "Difference"

set1 = {"a","b","c",1,2,8}
set2 = {1,2,3,4,5}

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)



set5 = set1.difference(set2)
print(set5)

