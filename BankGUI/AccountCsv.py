import csv
import os
import shutil
from PyQt5.QtCore import QDateTime
from BankWithDatabase.DatabaseMethods import update_customer_history, update_admin_history, get_admin_transactions_in_database, get_customer_transactions_in_database

admin_save_path = '../AdminHistoryFolder/'
user_save_path = '../UserHistoryFolder/'
user_deleted_save_path = '../UserHistoryFolder/DeletedUserFiles/'


def create_file():
    file = admin_save_path + 'Accounts.txt'
    if not os.path.exists(file):
        open(file, mode='a')


def move_file(username):
    file = user_save_path + f'{username}.txt'
    file2 = user_save_path + f'{username}1.txt'
    if not os.path.exists(user_deleted_save_path):
        os.makedirs(user_deleted_save_path)
    if os.path.exists(user_deleted_save_path + f'{username}.txt'):
        os.rename(file, file2)
        shutil.move(file2, user_deleted_save_path)
    else:
        shutil.move(file, user_deleted_save_path)


def get_account():
    file = admin_save_path + 'Accounts.txt'
    create_file()
    values = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            values.append(row)
    csv_file.close()
    return values


def edit_account(values):
    temp_file = admin_save_path + 'Temp.txt'
    file = admin_save_path + 'Accounts.txt'
    create_file()
    with open(temp_file, mode='a', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(values)
    new_file.close()
    os.remove(file)
    os.rename(temp_file, file)


def account_exists(username):
    users = []
    for user in get_account():
        users.append(user[1])
    if users.count(username):
        return True
    else:
        return False


def account_index(username):
    values = get_account()
    i = 0
    for value in values:
        if value[1] == username:
            return i
        else:
            i += 1


def delete_account(username):
    file = admin_save_path + 'Accounts.txt'
    temp_file = admin_save_path + 'Temp.txt'
    create_file()
    accounts = list()
    with open(file, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            accounts.append(row)
        i = 0
        for account in accounts:
            if account[1] == username:
                accounts.pop(i)
            else:
                i += 1
    with open(temp_file, mode='w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(accounts)
    os.remove(file)
    os.rename(temp_file, file)


def user_update_history(username, transaction, balance):
    today = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss ap')
    file = user_save_path + f'{username}.txt'
    if not os.path.exists(file):
        open(file, mode='a')
    if transaction == "Create Account":
        balance = "+" + balance
    elif transaction == "Delete Account":
        balance = "0"
    elif transaction == "Deposit":
        balance = "+" + balance
    elif transaction == "Withdraw":
        balance = "-" + balance
    values = [[today, transaction, balance]]
    with open(file, mode='a', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(values)
    update_customer_history(username, today, transaction, balance)


def admin_update_history(username, transaction):
    today = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss ap')
    file = admin_save_path + 'AdminHistory.txt'
    record = ""
    if not os.path.exists(file):
        open(file, mode='a')
    if transaction == "Add Account":
        record = f"Added new account with the username '{username}'"
    elif transaction == "Delete Account":
        record = f"Deleted account with the username '{username}'"
    values = [[today, record]]
    with open(file, mode='a', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(values)
    update_admin_history(today, record)


def get_admin_history(table):
    users = []
    values = []
    for items in get_admin_transactions_in_database(table):
        for item in items:
            values.append(str(item))
    users.append(values)
    return users

# print(get_admin_history("customer"))
def get_user_history(username):
    users = []
    values = []
    for items in get_customer_transactions_in_database(username):
        for item in items:
            values.append(str(item))
    users.append(values)
    return users
