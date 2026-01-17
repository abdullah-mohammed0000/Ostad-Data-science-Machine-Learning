guest = {
"name" : "Sarjis",
"Age" : "27",
"Favourite_item" : "Cake"
}

print("Guest Name :", guest["name"])
print("Favourite Snacks :", guest["Favourite_item"])

guest["Favourite_item"] = "Pasta"
print("Updated Snacks ", guest)

guest["Phone"] = "01234567888"
print("Updated Snacks ", guest)

del guest["Phone"]
print("Updated Snacks ", guest)

guest.pop("Age")
print("Updated Snacks ", guest)

guest.clear()
print("Updated Snacks ", guest)


#Looping in Dictionary

guest = {
    "name" : "Tarek",
    "age" : 61,
    "favourite item" : "Mojo" 
}

for ccc, ddd in guest.items():
    print(f"{ccc} : {ddd}")



party_guest = {
    "guest1" : {"Name" : "Tarek", "Snacks" : "Pasta"},
    "guest2" : {"Name" : "Nahid", "Snacks" : "Biriyani"},
    "guest3" : {"Name" : "Shafiq", "Snacks" : "Milk"}

}

print(party_guest["guest2"]["Name"])

for guest_id, details in party_guest.items():
    print(guest_id, "->", details["Name"], " loves ", details["Snacks"])