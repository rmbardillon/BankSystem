import mysql.connector


my_db = mysql.connector.connect(host="localhost", user="root", passwd="admin1234", database="atmsystem")
my_cursor = my_db.cursor()


def get_item(username, item):
    my_cursor.execute(f"SELECT {item} from customer where username='{username}'")
    for i in my_cursor:
        return i[0]


def account_is_existing(username):
    my_cursor.execute(f"SELECT EXISTS (SELECT * from customer where username='{username}')")
    for i in my_cursor:
        if int(i[0]) == 1:
            return True
        else:
            return False


def is_correct(username, pin):
    my_cursor.execute(f"SELECT pin from customer where username='{username}'")
    for i in my_cursor:
        if i[0] == pin:
            return True
        else:
            return False


def add_account(username, name, pin, balance):
    try:
        my_cursor.execute(f"INSERT into customer values('{username}','{name}', {pin}, {balance})")
        my_db.commit()
        return True
    except mysql.connector.errors.IntegrityError:
        return False


def delete_account_in_database(username):
    my_cursor.execute(f"DELETE from customer WHERE username='{username}'")
    my_db.commit()


def delete_account_transactions(username):
    my_cursor.execute(f"DELETE from customer_transactions WHERE username='{username}'")
    my_db.commit()


def deposit(username, money_deposited):
    balance = get_item(username, "balance")
    my_cursor.execute(f"UPDATE customer SET balance = {balance + money_deposited} where username='{username}'")
    my_db.commit()


def withdraw(username, money_withdrawn):
    balance = get_item(username, "balance")
    my_cursor.execute(f"UPDATE customer SET balance = {balance - money_withdrawn} where username='{username}'")
    my_db.commit()


def change_pin_in_database(username, new_pin):
    my_cursor.execute(f"UPDATE customer SET pin = {new_pin} where username='{username}'")
    my_db.commit()


def update_customer_history(username, today, transaction, balance):
    my_cursor.execute(f"INSERT into customer_transactions values('{username}', '{today}', '{transaction}', '{balance}')")
    my_db.commit()


def update_admin_history(today, transaction):
    my_cursor.execute(f'INSERT into admin_transactions values("{today}", "{transaction}")')
    my_db.commit()


def get_admin_transactions_in_database(table):
    values = []
    my_cursor.execute(f"SELECT * from {table}")
    for i in my_cursor:
        values.append(list(i))
    return values


def get_customer_transactions_in_database(username):
    values = []
    my_cursor.execute(f"SELECT date, transaction, balance from customer_transactions where username='{username}'")
    for i in my_cursor:
        values.append(list(i))
    return values
