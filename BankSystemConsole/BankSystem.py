from User import user_account
from Admin import admin_account

while True:
    choice = input("A. Admin\nB. User\t")
    if choice.upper() == "A":
        admin_account()
        break
    elif choice.upper() == "B":
        user_account()
        break
    else:
        print("Wrong Input! ")
