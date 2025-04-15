import os
import session
def login():
    session.username = input("Enter Username:").strip()
    if os.path.exists(os.path.join("users",session.username + ".txt")):
      print("USER EXISTS")
      file=open(os.path.join("users",session.username+".txt"),"r")
      session.password=input("Enter Password:")
      data=file.readlines()
      user_name=data[0].strip()
      user_password=data[1].strip()
      user_balance=int(data[2].strip())
      if session.password == user_password:
       print("WELCOME",user_name)
       file.close()
       return session.username,session.password,session.user_balance
      else:
       print("INVALID USRENAME OR PASSWORD")
       file.close()
    else:
      print("USER NOT FOUND PLEASE REGISTER")
    
    