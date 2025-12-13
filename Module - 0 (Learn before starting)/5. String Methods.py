#capitalize()	Converts the first character to upper case
a = "abdullah is doing ostad course"
print(a.capitalize())
print(a)

#casefold()	Converts string into lower case
b = "ABDULLAH IS DOING UDEMY COURSE"
print(b)
print(b.casefold())

#center()	Returns a centered string
c = "Ostad"
print(c.center(120))
print(c)

#count()	Returns the number of times a specified value occurs in a string
d = "Ostad is a good platform. I love ostad"
print(d.count("o")) #answer is 5
print(d.count("O")) #answer is 1

#encode()	Returns an encoded version of the string
e = "Udemy"
print(e.encode())



'''

s = "Udemy"
b = s.encode()        # b == b'Udemy'
print(type(b))        # <class 'bytes'>
print(b.decode())     # "Udemy"
print(list(b))        # [85, 100, 101, 109, 121]  (numeric byte values)


'''

#endswith()	Returns true if the string ends with the specified value
f = "Welcome to Ostad"
print(f.endswith("Ostad"))

#expandtabs()	Sets the tab size of the string
g= "H\te\tl\tl\to"
print(g.expandtabs(120))

#find()	Searches the string for a specified value and returns the position of where it was found
h = "Welcome to Ostad"
print(h.find("Ostad"))

#format()	Formats specified values in a string
i = "Welcome to {}. Enjoy your {} course."
print(i.format("Ostad", "Python"))

#format_map()	Formats specified values in a string
j = "Welcome to {platform}. Enjoy your {course} course."
print(j.format_map({"platform": "Ostad", "course": "Python"}))

#index()	Searches the string for a specified value and returns the position of where it was found
k = "Welcome to Ostad"
print(k.index("Ostad"))

#isalnum()	Returns True if all characters in the string are alphanumeric
l = "Ostad2025"
print(l.isalnum())



#isalpha()	Returns True if all characters in the string are in the alphabet
m = "Ostad686987"
print(m.isalpha())


#isascii()	Returns True if all characters in the string are ASCII characters

n = "Ostad434"
print(n.isascii())

#isdecimal()	Returns True if all characters in the string are decimals
o = "123456"
print(o.isdecimal())

#isdigit()	Returns True if all characters in the string are digits
p = "1234o"
print(p.isdigit())

#isidentifier()	Returns True if the string is an identifier
q = "Ostad_2024"
print(q.isidentifier())

#islower()	Returns True if all characters in the string are lower case
r = "oStad"
print(r.islower())

#isnumeric()	Returns True if all characters in the string are numeric
s = "12345"   
print(s.isnumeric())

#isprintable()	Returns True if all characters in the string are printable
t = "Ostad\n"
print(t.isprintable())

#isspace()	Returns True if all characters in the string are whitespaces
u = "    "
print(u.isspace())

#istitle()	Returns True if the string follows the rules of a title
v = "Ostad Is The Best"
print(v.istitle())

#isupper()	Returns True if all characters in the string are upper case
w = "OSTAD"
print(w.isupper())

#join()	Joins the elements of an iterable to the end of the string
x = "-".join(["Ostad", "is", "the", "best"])
print(x)

#ljust()	Returns a left justified version of the string
y = "Ostad"
print(y.ljust(120))
print(y)

#lower()	Converts a string into lower case
z = "OSTAD"
print(z.lower())

#lstrip()	Returns a left trim version of the string
a1 = "   Coursera   f" 
print(a1.lstrip())

#maketrans()	Returns a translation table to be used in translations
s = "abcdef"
print(s.maketrans("abc", "123"))  # {97: 49, 98: 50, 99: 51}
table = s.maketrans("abc", "123")
print(s.translate(table))  # "123def"

#partition()	Returns a tuple where the string is parted into three parts
a2 = "I love Ostad platform"
print(a2.partition("Ostad"))

#replace()	Returns a string where a specified value is replaced with a specified value
a3 = "I love Ostad platform"
print(a3.replace("Ostad", "Udemy")) 

#rfind()	Searches the string for a specified value and returns the last position of where it was found
a4 = "Welcome to Ostad. Ostad is to the best platform."    
print(a4.rfind("to"))

#rindex()	Searches the string for a specified value and returns the last position of where it was found
a5 = "Welcome to Ostad. Ostad is to the best platform."
print(a5.rindex("Ostad"))

#rjust()	Returns a right justified version of the string
a6 = "Ostad"
print(a6.rjust(120))    



#rpartition()	Returns a tuple where the string is parted into three parts
a7 = "I love Ostad platform"    
print(a7.rpartition("Ostad"))

#rsplit()	Splits the string at the specified separator, and returns a list
a8 = "apple, banana, cherry, date"  
print(a8.rsplit(", ", 2))  # ['apple, banana', 'cherry', 'date']

#rStrip()	Returns a right trim version of the string
a9 = "  Coursera              "
print(a9.rstrip())

#split()	Splits the string at the specified separator, and returns a list

a10 = "apple, banana, cherry, date"
print(a10.split(", ", 2))  # ['apple', 'banana', 'cherry, date']


#splitlines()	Splits the string at line breaks and returns a list
a11 = "Hello World!\nWelcome to Ostad.\nEnjoy your course."
print(a11.splitlines())

#startswith()	Returns true if the string starts with the specified value
a12 = "Welcome to Ostad"    
print(a12.startswith("Welcome"))

#strip()	Returns a trimmed version of the string
a13 = "   Coursera   "  
print(a13.strip())  

#swapcase()	Swaps cases, lower case becomes upper case and vice versa
a14 = "Hello World!"    
print(a14.swapcase())

#title()	Converts the first character of each word to upper case
a15 = "welcome to ostad platform"   
print(a15.title())

#translate()	Returns a translated string
a16 = "abcdef"
table = a16.maketrans("abc", "123")
print(a16.translate(table))  # "123def"

#upper()	Converts a string into upper case
a17 = "ostad"
print(a17.upper())

#zfill()	Fills the string with a specified number of 0 values at the beginning
a18 = "42"  
print(a18.zfill(8))  # "00042"