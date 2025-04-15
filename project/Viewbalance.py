from Login import login
import os
import session
def viewbalance():
  if session.username == None:
    print("Please log in first")
  else:
    file = open(os.path.join("users",session.username + ".txt"),"r")
    data=file.readlines()
    session.userbalance=int(data[2].strip())
    file.close()
    print("Your current balance is",session.userbalance)