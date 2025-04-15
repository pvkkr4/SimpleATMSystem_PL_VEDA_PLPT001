from Login import login
import os
import session
import time
def deposit():
    if session.username != None:
        pas=input("Enter password: ")
        if(str(pas) == session.password):
            amount = int(input("Enter amount to deposit: "))
            file = open(os.path.join("users",session.username + ".txt"),"r")
            data = file.readlines()
            session.user_balance = int(data[2].strip())
            session.user_balance += amount
            data[2] = str(session.user_balance)+"\n"
            file.close()
            file = open(os.path.join("users",session.username + ".txt"),"w")
            file.writelines(data)
            file.close()
            file = open(os.path.join("users",session.username + ".txt"),"a")
            file.write("\n")
            file.write(session.username+" Deposit of "+str(amount)+" on "+time.asctime()+"\n")
            file.close()
            print("Deposit successful. New balance is:", session.user_balance)
        else:
         print("Password is incorrect.Please check again or Login first")
    else:
        print("Please login first")
