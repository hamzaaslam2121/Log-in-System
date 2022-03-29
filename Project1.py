"""Creating a Log-in System"""

import sqlite3

accountsdb = sqlite3.connect(':memory:')

cursor1 = accountsdb.cursor()

cursor1.execute("""CREATE TABLE users (
            username TEXT,
            password TEXT);""")        


user_name = input('Please enter your username: ')
pass_word = input('Please enter your password: ')


def database_check(user):   # function for checking whether entered "username" and "password" is already present in database
    cursor1.execute("""SELECT username, password 
            FROM accountsdb WHERE username=?, password=?""",
            (user_name, pass_word))     

    result = cursor1.fetchone()
    username_check = cursor1.fetchone(username)

    if result is None:
        cursor1.execute("""INSERT INTO accountsdb (username, password) VALUES (?,?)""", (user_name, pass_word))
        accountsdb.commit
        print("Welcome to my Log-In System, a new account has been created!")
    elif username_check == 1:
        print("Password incorrect, please re-try.")
    else: 
        return ('Success. Welcome',{}.format(user_name),'!')

accountsdb.close()