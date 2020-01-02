#!/usr/bin/python3

#program similar to cat command
y=input('Enter the name of the file you want to see the content of: ')

#opening file y
f=open(y)

#reading content of the file
text=f.read()

#printing content of the file
print(text)

#closing file
f.close
