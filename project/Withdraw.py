from Login import login
import session
import os
import time
def withdraw():
  if (session.password == None) :
    print("Please login first")
    return
  passw=input("ENTER YOUR PASSWORD: ")
  if(session.password == passw):
    amount=int(input("Enter amount to withdraw: "))
    file=open(session.username+".txt","r")
    data=file.readlines()
    session.user_balance=int(data[2].strip())
    if(session.user_balance == 0 or session.user_balance<amount):
      print("You do not have enough money in your account")
      file.close()
    else:
        session.user_balance -= amount
        data[2] = str(session.user_balance) + "\n"
        file.close()
        file=open(session.username+".txt","w")
        file.writelines(data)
        file.close()
        file=open(session.username+".txt","a")
        file.write(str(session.username) +" has withdrawn "+str(amount)+" on "+time.asctime()+"\n")
        file.close()
        print("Withdraw successful. New balance is:", session.user_balance)
  else:
    print("Password is incorrect")
    
    
    
  