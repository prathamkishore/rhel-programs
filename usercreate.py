#!/usr/bin/python3
import subprocess,time
while 1:
     option="""choose from the following to create a user:-
     press 1 to create a user-
     press 2 to Add password to the user-
     press 3 to change password of a existing user-
     press 4 to delete any user-
     press 5 to exit-
     """
     print(option)
     choice=input()
     if choice == '1':
         name=input("Enter user name:-")
         print("Creating user  "+name)
         out=subprocess.getstatusoutput("useradd "+name)
         if out[0] == 0:
          print('user created successfully... ')
         else:
          out=subprocess.getoutput("whoami")
          if out == 'root':
           print("user already exists")
           exit()
          else:
           print("you do not have Admin Priviledges...")
           exit()
         p=input("would like to give a password YES/NO:-")
         if p == 'yes':
             print("now type password hit enter then again type password")
             print(subprocess.getoutput("passwd "+name))
             out=subprocess.getstatusoutput("passwd "+name)
     elif choice =='2':
         name=input("Enter user name :-")
         print("now type password hit enter then again type password")
         print(subprocess.getoutput("passwd "+name))
         out=subprocess.getstatusoutput("passwd "+name)
         if out[0] == 0:
           print('enter password ')
         else:
           print("user not found")
     elif choice =='3':
         name=input("Enter user name :-")
         print("now type password hit enter then again type password")
         print(subprocess.getoutput("passwd "+name))
         out=subprocess.getstatusoutput("passwd "+name)
         if out[0] == 0:
           print('enter password ')
         else:
           print("user not found")

     elif choice =='5':
         exit()
     if choice == '4':
         name=input("Enter user name:-")
         print("Deleting user  "+name)
         out=subprocess.getstatusoutput("userdel "+name)
         if out[0] == 0:
          print('user deleted successfully... ')
         else:
          out=subprocess.getoutput("whoami")
          if out == 'root':
           print("user doesn't exists")
           exit()
          else:
           print("you do not have Admin Priviledges...")
           exit()
           
     else:
         print("choose a valid option")
