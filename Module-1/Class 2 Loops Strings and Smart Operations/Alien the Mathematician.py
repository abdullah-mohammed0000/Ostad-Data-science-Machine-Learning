import math 

distance_to_home = 384400
gravity = 9.8

thrust_needed = math.sqrt(distance_to_home*gravity)
print(round(thrust_needed))

base_length =  10
height = 15
area = 0.5 * base_length * height
print(area)

angle_radians = math.atan(height/base_length)
print(angle_radians)

angle_degree = math.degrees(angle_radians)
print(angle_degree)


x = 5.1
print(math.ceil(x))

y = 5.99
print(math.floor(y))