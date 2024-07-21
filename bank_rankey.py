import random

pass_code="2205"
def show_balance(balance):
    PIN_num=input("Enter the Four digit number: ")
    if PIN_num== pass_code:
        pass
    else:
        print("Incorrect PIN numbers")
        is_running=False
    print(f"your balance is ${balance: 2f}")
def deposit():
    amount=float(input("Enter your amount to be deposited: "))
    if amount <0:
        print("Enter a valid amount")
    else:
        PIN_num=input("Enter the Four digit number: ")
        if PIN_num== pass_code:
            pass
        else:
            print("Incorrect PIN numbers")
            is_running=False
        return amount
def withdraw(balance):
    amount=float(input("Enter your withdrawal amount : "))
    if amount <0:
        print("Enter a valid amount")
    elif amount> balance:
        print("Insufficient balance")
    else:
        PIN_num=input("Enter the Four digit number: ")
        if PIN_num== pass_code:
            pass
        else:
            print("Incorrect PIN numbers")
            is_running=False
        return amount

class main():

    balance=0
    is_running=True

    while is_running :
        print("1) Show Balance")
        print("2) Deposit ")
        print("3) withdraw")
        print("4) Exit ")
        choice=input("Enter your choice: ")
        if choice=="1":
            show_balance(balance)
        elif choice=="2":
            balance += deposit()
            print(f"your amount is deposited")
            print(f"your balance is {balance}")
        elif choice == "3":
            balance -= withdraw(balance)
            print(f"your amount has been withdrawn")
            print(f"your balance is {balance}")
        elif choice=="4":
            print("Thank you!")
            is_running=False
        else:
            print("Please press the valid option")

if __name__=="__main__":
    main()
