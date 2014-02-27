#ex16_1.py
from sys import argv
app,filename=argv
file1=open(filename)

#print the file content
buffer =file1.read()
print buffer
