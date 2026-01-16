# errors vs exception

# Compile Time, Run Time
# Errors --> Compile Time or error
#        --> Syntax, Introduction
#Exceptions --> Run Time Error
#            --> Indexing, key, value, zero division


try: #je code e exception thakte pare
 with open("rahim.txt", 'r') as f:
      print(f.read())

except FileNotFoundError:
   print("File Not Found")



try: #je code e exception thakte pare
 with open("name.txt", 'r') as f:
      print(f.read())

except FileNotFoundError:
   print("File Not Found")