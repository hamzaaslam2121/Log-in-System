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
    cursor1.execute("""SELECT password 
            FROM users WHERE username=?""",
            (user_name,))
    
    
    try:
        result = cursor1.fetchone()[0]
        

        if result == pass_word:
            return ('Success. Welcome {}!'.format(user_name))
    
        else:
            return 'Password incorrect. Please re-try'


    except TypeError: 
        cursor1.execute("""INSERT INTO users (username, password) VALUES (?,?)""", (user_name, pass_word))
        accountsdb.commit()
        return("A new account has been created!")

  


print(database_check(user_name, pass_word)) 

accountsdb.close()




