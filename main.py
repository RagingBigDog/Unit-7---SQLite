# imports sqllite3
import sqlite3

# creates a connection to the database and creates it if it is not present
connection = sqlite3.connect("contacts.db")

# create a cursor to execute sql statements
crsr = connection.cursor()

# creates a table using the requirements for the homework
crsr.execute('''CREATE TABLE contacts (ContactID int primary key, FirstName char(50), 
LastName char(50), PhoneNumber char(15), EmailAddress char(50))''')

# insets values into the empty table
crsr.execute('''INSERT INTO contacts VALUES 
(1, "Morty", "Smith", 5553331111, "msmith@gmail.com"), 
(2, "Beth", "Smith", 8885557979, "bsmith@gmail.com"), 
(3, "Summer", "Smith", 3331535555, "ssmith@gmail.com"), 
(4, "Rick", "Smith", 5556969696, "dontemailme@gmail.com"), 
(5, "Jerry", "Smith", 4436715555, "jsmith@gmail.com")''')

# commits the current changes
connection.commit()

# selects all the columns from the table contacts
crsr.execute('''SELECT * FROM contacts''')

# saves the select statement to a list called results
results = crsr.fetchall()

# prints each item in the list
for x in results:
    print(x)

# prints a new line for formatting
print("\n")

# selects only the FirstName, LastName, and EmailAddress columns from the table contacts
crsr.execute('''SELECT FirstName, LastName, EmailAddress FROM contacts''')

# updates the contact's mail and phone number whose ID is 4
crsr.execute('''UPDATE contacts SET EmailAddress = "notrick@gmail.com", PhoneNumber = 6965558008 WHERE ContactID = 4''')

# deletes the last contact that was entered, which has an ID of 5
crsr.execute('''DELETE FROM contacts WHERE ContactID = 5''')

# selects all the columns from the table contacts
crsr.execute('''SELECT * FROM contacts''')

# saves the select statement to a list called results
results = crsr.fetchall()

# prints each item in the list
for x in results:
    print(x)

# commits the current changes
connection.commit()

# closes the connection to the database
connection.close()