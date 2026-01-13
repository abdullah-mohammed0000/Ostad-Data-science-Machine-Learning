Tweet = "I have fb, insta, tiktok, pinterest, twitter and youtube account"

print(Tweet[0:5])
print(Tweet[:7])

messy = "I Love My country#####so much!!!!!!!"
cleaned = messy.replace('#', "").replace("!","")
print(cleaned)

print("Capitalized: ",cleaned.capitalize())
print("Upper: ",cleaned.upper())
print("Lower: ",cleaned.lower())


planet = "Earth"
Temperature = 30.987980789
Weather = "Cold"

report = "Planet: {}, Temp: {:.2f} degree, Weather: {}".format(planet,Temperature,Weather)
print(report)

print(f"Planet {planet}, Temp {Temperature:.1f} degree, Weather {Weather}")
