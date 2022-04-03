"""Creating a Log-in System"""

import sqlite3

accountsdb = sqlite3.connect('/Users/hamzaaslam/CompSci/Python/Projects/Project1/Log-in-system-Project/accounts.db')

cursor1 = accountsdb.cursor()


user_name = input(str('Please enter your username: ')) # these are the inputs i put into the function (use as args)
pass_word = input(str('Please enter your password: '))

cursor1.execute("""CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT);""")        


def database_check(user_name, pass_word):   # function for checking whether entered "username" and "password" is already present in database
    cursor1.execute("""SELECT username, password 
            FROM users WHERE username=? AND password=?""",
            (user_name, pass_word))
    
    result = cursor1.fetchone()
    username_check = result[0]
    

    if username_check == True :
        return("Password incorrect, please re-try.")
    elif result is None:
        cursor1.execute("""INSERT INTO users (username, password) VALUES (?,?)""", (user_name, pass_word))
        accountsdb.commit
        return("Welcome to my Log-In System, a new account has been created!")
    else: 
        return ('Success. Welcome {}!'.format(user_name))


print(database_check(user_name, pass_word)) 

accountsdb.close()




