from time import sleep
from ClearScreen import clear
from Checker import float_validator, pin_validator
balance = 10000
user_pin = 1234


def format_float(float_balance):
    return "₱{:,.2f}".format(float_balance)


def account_balance():
    print(f"Your balance is {format_float(balance)}")
    sleep(2)
    clear()


def deposit():
    global balance
    print(f"Your Balance is {format_float(balance)}")
    money_deposited = float_validator("How much money you want to deposit?\n")
    balance += money_deposited
    print(f"You deposited {format_float(money_deposited)}.\nYour new balance is {format_float(balance)}")
    sleep(2)
    clear()


def withdraw():
    global balance
    print(f"Your Balance is {format_float(balance)}")
    while balance > 0:
        while True:
            money_withdrawn = float_validator("How much money you want to withdraw?\n")
            if money_withdrawn > balance:
                print("You don't have enough balance.")
                sleep(2)
            else:
                balance -= money_withdrawn
                print(f"You withdrawn {format_float(money_withdrawn)}.\nYour new balance is {format_float(balance)}")
                sleep(2)
                clear()
                break
        break


def change_pin():
    global user_pin
    while True:
        new_pin = pin_validator("Input your new pin: ")
        confirm_pin = pin_validator("Confirm your new pin: ")
        if new_pin == confirm_pin:
            user_pin = new_pin
            print(f"Pin was changed. Your new pin is {user_pin}")
            break
        else:
            print("Pin didn't matched.")
    sleep(2)
    clear()


def pin_checker(pin):
    if user_pin == pin:
        return True
    else:
        return False
