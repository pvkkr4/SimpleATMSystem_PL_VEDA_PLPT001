from Login import login
import session
def viewbalance():
  if session.username == None:
    print("Please log in first")
  else:
    file=open(session.username+".txt","r")
    data=file.readlines()
    session.userbalance=int(data[2].strip())
    file.close()
    print("Your current balance is",session.userbalance)