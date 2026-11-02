balance=5000
pin=1234
attempts=3
daily_limit=2000
transactions=[]
def check_balance():
    print("Current Balance:",balance)
def deposit_money():
    global balance
    amount=int(input("Enter deposit amount:"))
    if amount>0:
       balance+=amount 
       transactions.append(f"Deposited:{amount}")
       print("Deposit successful")
    else:
       prin("Invalid amount")
def withdraw_money():
    global balance
    amount=int(input("Enter withdrawal amount:"))
    if amount>daily_limit:
       print("Daily limit exceeded")
    elif amount<=0:
       print("Invalid amount")
    else:
       balance-=amount 
       transactions.append(f"Withdrawn:{amount}")
    print("please collect your cash")
def mini_statement():
    if not transactions:
       print("No transactions yet")
    else:
       print("Mini Statement")
       for t in transactions:
          print("-",t)
#PIN CHECK
while attempts>0:
  user_pin=int(input("Enter your pin:"))
  if user_pin==pin:
     print("Login Successful")
     break
  else:
     attempts-=1
     print("Wrong PIN.Attempt left:",attempts)
if attempts==0:
   print("Card blocked")
else:
  while True:
    print("\n1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Mini Statemnt")
    print("5.Exit")
    choice=int(input("choose option:"))
    if choice==1:
       check_balance()
    elif choice==2:
       deposit_money()
    elif choice==3:
       withdraw_money()
    elif choice==4:
       mini_statement()
    elif choice==5:
       print("Thank you for using ATM")
       break
    else:  
       print("Invalid option")	
