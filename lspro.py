#!/usr/bin/python3

#importing nessecary modules 
#pprint is to print contents is a list format
import os
from pprint import pprint


#taking input name of directory
x=input("Enter name of the Directory : ")

#os command similar to ls command
dirlist=os.listdir(x)

#printing contents
pprint(dirlist)

