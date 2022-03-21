# Log-in System
A python project.

System will ask user to input a username and password. If the system does not recognise the username, then the system will instead ask user to create a new username and password (account). It will then store these details allowing the user to correctly log in next time.

If the user inputs password incorrectly, the system will ask the user to re-try. There will be a re-try limiter of 3 times, before a 30 second cooldown will be initiated. 

If both username and password are entered correctly, then the system will proceed sending a "Success, Welcome 'User'!" message. 
