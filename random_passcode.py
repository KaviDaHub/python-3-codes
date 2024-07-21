import random
password=""
is_running=True
while is_running :
    password="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqqrstuvwxyz!@#$%^&*()_+}{:[]?/>.<,~"
    password_length=int(input("Enter the length of password : "))
    a="".join(random.sample(password,password_length))
    print(f"your generated strong password is {a}")
