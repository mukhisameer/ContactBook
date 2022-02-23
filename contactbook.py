import mysql.connector

# Connector to communicate with the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="*********",
    database="contactBook"
)

cursor = db.cursor()

# Code to create the database initially
# cursor.execute("CREATE DATBASE contactBook")

#Code to create the table initially
# cursor.execute("CREATE TABLE Contacts (personID int PRIMARY KEY AUTO_INCREMENT, firstName VARCHAR(50), lastName VARCHAR(50), number VARCHAR(15), email VARCHAR(100))")

# A display menu to enable user to interact with the program
def displayMenu():
    action = input('Contact Book\nChoose one of the following actions to perform\n1. Add a contact\n2. View all Contacts\n3. Search for a contact\n4. Delete a contact\n5. Edit a contact\n6. Exit\n\nPlease enter the number associated with the actions: ')
    print()
    if action == '1':
        addContact()
    elif action == '2':
        printAllContacts()
    elif action == '3':
        searchContact()
    elif action == '4':
        deleteContact()
    elif action == '5':
        editContact()
    elif action == '6':
        exit()

# Function to add a contact to the contact book
def addContact():
    print("Please provide the following details to add a contact.")
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    number = input("Phone Number: ")
    email = input("Email: ")

    cursor.execute("INSERT INTO Contacts (firstName, lastName, number, email) Values (%s, %s, %s, %s)", (firstName, lastName, number, email))
    db.commit()
    print()
    print("Contact added succesfully.")
    print()

# Function to view all contacts
def printAllContacts():
    cursor.execute("SELECT * FROM Contacts")
    count = 0
    for contact in cursor:
        count+=1
    if count == 0:
        print("No contacts found.")
    else:
        cursor.execute("SELECT * FROM Contacts")
        for contact in cursor:
            print(contact)
    print()

# Function to search for a contact
def searchContact():
    action = input('Search Using: \n1. First Name\n2. Last Name\n3. Phone Number\n4. Email\nPlease enter the number associated with the actions: ')
    print()
    if action == '1':
        searchTerm = input('Please enter the first name: ')
        cursor.execute("Select * FROM Contacts WHERE firstName = %s", (searchTerm, ))
    elif action == '2':
        searchTerm = input('Please enter the last name: ')
        cursor.execute("Select * FROM Contacts WHERE lastName = %s", (searchTerm, ))
    elif action == '3':
        searchTerm = input('Please enter the number: ')
        cursor.execute("Select * FROM Contacts WHERE number = %s", (searchTerm, ))
    elif action == '4':
        searchTerm = input('Please enter the email: ')
        cursor.execute("Select * FROM Contacts WHERE email = %s", (searchTerm, ))
    count = 0
    for contact in cursor:
        count+=1
    if count == 0:
        print("No contacts found.")
    else:
        cursor.execute("SELECT * FROM Contacts")
        for contact in cursor:
            print(contact)
    print()

# Function to delete a contact
def deleteContact():
    print("How would you like to search for the contact to delete?")
    searchContact()
    searchTerm = int(input("Please input the number associated with the contact you wish to delete: "))
    cursor.execute("DELETE FROM Contacts WHERE personID = %s", (searchTerm, ))
    db.commit()
    print("Contact deleted succesfully.")
    print()

# Function to edit a contact
def editContact():
    print("How would you like to search for the contact to edit?")
    searchContact()
    contactID = int(input("Please input the number associated with the contact you wish to edit: "))
    print()
    detail = input('Select the contact detail you would like to update: \n1. First Name\n2. Last Name\n3. Phone Number\n4. Email\nPlease enter the number associated with the detail: ')
    value = input("Please enter the new value for the detail: ")

    if detail == '1':
        cursor.execute("UPDATE Contacts SET firstName = %s WHERE personID = %s", (value, contactID))
    elif detail == '2':
        cursor.execute("UPDATE Contacts SET lastName = %s WHERE personID = %s", (value, contactID))
    elif detail == '3':
        cursor.execute("UPDATE Contacts SET number = %s WHERE personID = %s", (value, contactID))
    elif detail == '4':
        cursor.execute("UPDATE Contacts SET email = %s WHERE personID = %s", (value, contactID))
    
    print()
    print("Contact updated succesfully.")
    print()

# Main function that continuesly runs displayMenu() until the user decides to exit the program
def main():
    while True:
        displayMenu()
        
main()