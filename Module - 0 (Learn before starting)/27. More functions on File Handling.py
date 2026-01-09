import os
import pathlib

if os.path.exists('name.txt'):
    print("File exists")

else:
    print("File not found")


file_path = pathlib.Path('name.txt')

if file_path.exists():
    print("File exists")
print(os.path.abspath('name.txt'))
print(os.path.getsize('name.txt'))

with open('name.txt', 'r') as f:
    print(f.read(5))

