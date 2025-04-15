from Login import login
from Register import register
from Deposit import deposit
from Viewbalance import viewbalance
from Withdraw import withdraw
def menu():
  while True:
    print("1. Register")
    print("2. Login")
    print("3. View current balance")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
      register()
    elif choice==2:
      login()
    elif choice==3:
     viewbalance()
    elif choice==4:
      deposit()
    elif choice==5:
      withdraw()
    elif choice==6:
      print("Thank you for using our service")
      break
    else:
      print("Invalid choice, please try again")
menu()

















































































































