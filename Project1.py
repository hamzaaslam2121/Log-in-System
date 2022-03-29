"""Creating a Log-in System"""

import sqlite3

accountsdb = sqlite3.connect(':memory:')

cursor1 = accountsdb.cursor()

cursor1.execute("""CREATE TABLE users (
            username VARCHAR,
            password VARCHAR)""")        


 



username = input('Please enter your username ')
password = input('Please enter your password ')



def database_check(user):   # function for checking whether entered "username" and "password" is already present in database
    cursor1.execute("""SELECT username, password 
            FROM accountsdb WHERE username=?, password=?""",
            (email, password))     

    result = cursor1.fetchone()
    username_check = cursor1.fetchone(username)

    if len(result)==0:
        cursor1.execute("""INSERT INTO accountsdb VALUES (?,?)""", (username, password))
        print("Welcome to my Log-In System, a new account has been created!")
    elif username_check == 1:
        print("Password incorrect, please re-try.")
    else: 
        return ('Welcome',{}).format(username)

    