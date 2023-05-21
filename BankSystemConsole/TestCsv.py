from BankGUI.AccountCsv import get_account, add_account

new_user = []
print(get_account('Accounts.txt'))
username = input("Username: ")
pin = input("Pin: ")
balance = input("Balance: ")
new_user.append(username)
new_user.append(pin)
new_user.append(balance)
existing_users = get_account("Accounts.txt")
existing_users.append(new_user)
add_account(existing_users, "Accounts.txt")