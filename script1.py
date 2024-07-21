def fav_food(food):
    print(f"your fav food is {food}")
def user_name(name):
    print(f"your username: {name}")
    print(f"goodbye! {name}")
def main():
    print("its script 1")
    fav_food(input("food: "))
    user_name(input("name: "))
if __name__=='__main__':
    main()