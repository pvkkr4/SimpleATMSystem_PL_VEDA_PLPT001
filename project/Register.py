import os
import shutil
import session
def register():
  user = input("Enter username: ")
  if os.path.exists(os.path.join("users", user + ".txt")):
    print("User exists")
    print("Please login or choose other username")
  else:
    password = input("Enter password: ")
    if password == None:
      print("Password cannot be empty")
    else:
      session.username=user
      session.password=password
      file = open(user+".txt", "w")
      file.write(user+"\n"+password+"\n"+"0"+"\n")
      file.close()
      for file_name in os.listdir("."):
            if file_name.endswith(".txt"):
                shutil.move(os.path.join(".", file_name),
                            os.path.join("users", file_name))
