import os
def register():
  user = input("Enter username: ")
  if os.path.exists(user+".txt"):
    print("User exists")
    print("Please login or choose other username")
  else:
    password = input("Enter password: ")
    if password == None:
      print("Password cannot be empty")
    else:
      file = open(user+".txt", "w")
      file.write(user+"\n"+password+"\n"+"0"+"\n")
      file.close()