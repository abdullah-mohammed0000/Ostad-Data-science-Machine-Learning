distance_to_home = 384400 #in km
fuel_efficiency = 0.5

fuel_needed = distance_to_home * fuel_efficiency
print("Fuel Needed: ", fuel_needed, "units\n")

#By taking input

distance_to_home = int(input("Enter total distance to home: "))
fuel_efficiency = int(input("Fuel Efficiency: "))

fuel_needed = distance_to_home * fuel_efficiency
print("Fuel Needed: ",fuel_needed, "units\n")

#Alien's Eating

chocolate = 3
sprinkle = 2
price_choco = 5
price_sprinkle = 6

Total = chocolate * price_choco + sprinkle * price_sprinkle
print("Total Expense: ", Total, "$")

tax = Total * 0.10
print("Total with tax: ", Total + tax, "$")

#PEMDAS OR BODMAS

result = 100 - 20/(4*5)

print(result)


#Food Distribution
total_slices = 8
aliens = 3

slices_per_alien = total_slices/aliens
print("Slieces Per Alien will get: ", slices_per_alien)

print("Full Slices they get: ", total_slices//aliens)

print("Left Over: ", total_slices%aliens)


#Star

asteroid_Sites = [34,7,108, 55,2,89]
smallest = min(asteroid_Sites)
largest = max(asteroid_Sites)

print("Smallest Size: ", smallest)
print("Largest Size: ", largest)


#Power Calculation

base = 3
exponent = 4

power_calculation = pow(base,exponent)
print(power_calculation)
