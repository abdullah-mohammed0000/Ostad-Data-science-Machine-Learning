#It will replace text file with new text
#with open ('25(1). name.txt', 'w') as f:
  #f.write("Biggest superstar in Bangladesh\n")
  #f.write("Bangladesh is a beautiful country\n")

  #But this will not replace text file rather it will add new text at the end of the file
with open ('25(1). name.txt', 'a') as f:
   f.write("Biggest superstar in Bangladesh\n")
   f.write("Bangladesh is a beautiful country\n")

   ###
   lines = ['I love my country\n', 'I love my people\n']

   with open ('25(1). name.txt', 'a') as f:
      f.writelines(lines)