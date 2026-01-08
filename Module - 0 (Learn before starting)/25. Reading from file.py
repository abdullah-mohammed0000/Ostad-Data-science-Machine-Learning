file = open('25(1). name.txt','r')
content = file.read()
print(content)
file.close()



with open('25(1). name.txt', 'r') as f:
  content = f.read()
  print(content)