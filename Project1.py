"""Creating a Log-in System"""

import sqlite3
import bcrypt

accountsdb = sqlite3.connect('/Users/hamzaaslam/CompSci/Python/Projects/Project1/Log-in-system-Project/accounts.db')

cursor1 = accountsdb.cursor()


user_name = input(str('Please enter your username: ')) # these are the inputs i put into the function (use as args)
pass_word = input(str('Please enter your password: '))
bpass_word = pass_word.encode('utf-8')

hashedpass = bcrypt.hashpw(bytes(pass_word.encode('utf-8')), bcrypt.gensalt(rounds=12))


cursor1.execute("""CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT,
            UNIQUE(username));""") 



def database_check(user_name, hashedpass):   
        cursor1.execute("""SELECT password 
            FROM users WHERE username=?""",
            (user_name,))

        result = cursor1.fetchone()

        if result is None:
            cursor1.execute("""INSERT OR IGNORE INTO users (username, password) VALUES (?,?)""", (user_name, hashedpass))
            accountsdb.commit()
            return("A new account has been created!")

        elif bcrypt.checkpw(bpass_word, result[0]) is not True:
            return 'Password incorrect. Please re-try'
  
        else:
            return ('Success. Welcome {}!'.format(user_name))            
   

  
print(database_check(user_name, hashedpass)) 

accountsdb.close()




