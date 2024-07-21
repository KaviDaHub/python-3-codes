import pyttsx3
def Happy_Birthday(name,age):
    print(f"Happy birthday to {name}!")
    print(f"you are {age} years old ")
    print()
Happy_Birthday("kavid",21)
Happy_Birthday("praneel",1)
Happy_Birthday("Athirankutyy",1)
def invoice_message(name,amount,date):
    print(f"hello dear {name} !")
    print(f"your bill of $ {amount: 2f} is on due date {date}")
    print()
invoice_message("kavid",2,"1/1/2001")
#return function
def add(x,y):
    z=x+y
    return z
def multiple(x,y):
    z=x*y
    return z
print(add(2,5))
print(multiple(2,5))
def full_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    full_name=print(first+" "+last)
print(full_name("kavidurga","vaiyapuri"))
def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last
full_name=create_name("kavidurga","vaiyapuri")
print(full_name)
