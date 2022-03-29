"""Creating a Log-in System"""

import sqlite3

accountsdb = sqlite3.connect(':memory:')

cursor1 = accountsdb.cursor()

cursor1.execute("""CREATE TABLE users(
            username TEXT,
            password TEXT);""")        


def database_check(user_name, pass_word):   # function for checking whether entered "username" and "password" is already present in database
    cursor1.execute("""SELECT username, password 
            FROM users WHERE username=? OR password=?""",
            (user_name, pass_word))

    result = cursor1.fetchone()
    username_check = cursor1.fetchone(user_name)

    if result is None:
        cursor1.execute("""INSERT INTO users (username, password) VALUES (?,?)""", (user_name, pass_word))
        accountsdb.commit
        print("Welcome to my Log-In System, a new account has been created!")
    elif username_check == 1:
        print("Password incorrect, please re-try.")
    else: 
        return ('Success. Welcome',{}.format(user_name),'!')

user_name = input(str('Please enter your username: ')) # these are the inputs i wish to put into the function (use as args)
pass_word = input(str('Please enter your password: '))

print(database_check(user_name, pass_word)) 

accountsdb.close()