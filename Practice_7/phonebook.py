import csv
from connect import get_connection
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        number VARCHAR(255) NOT NULL
    );
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def add_information():
    name = input("Enter name: ").strip()
    number = input("Enter phone: ").strip()
    query = """
        INSERT INTO phonebook (first_name, phone)
        VALUES (%s, %s);
        """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, (name, number))
    connection.commit()
    connection.close()

def insert_from_csv(filename="contacts.csv"):
    query = """
        INSERT INTO phonebook (first_name, phone)
        VALUES (%s, %s);
        """
    connection = get_connection()
    cursor = connection.cursor()
    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["first_name"].strip()
            number = row["phone"].strip()
            cursor.execute(query, (name, number))

        connection.commit()
        print("Contacts imported successfully.")

def delete_contact():
    query = """
    DELETE FROM phonebook
    where phone = %s;
    """
    connection = get_connection()
    cursor = connection.cursor()
    name = input("Enter number: ").strip()
    cursor.execute(query, (name))
    connection.commit()
    connection.close()
    cursor.close()
    print("Contact deleted successfully.")

def update_contact():
    query = """
    UPDATE phonebook
    SET phone = %s
    WHERE phone = %s;
    """
    connection = get_connection()
    cursor = connection.cursor()
    old_number = input("Enter old name: ").strip()
    new_number = input("Enter new name: ").strip()
    cursor.execute(query, (old_number,new_number))
    connection.commit()
    connection.close()
    cursor.close()
    print("Contact updated successfully.")
def find_contact():
    def find_contact():
        query = """
        SELECT * FROM phonebook
        WHERE number = %s;
        """
        connection = get_connection()
        cursor = connection.cursor()

        number = input("Enter number: ").strip()
        cursor.execute(query, (number,))

        contact = cursor.fetchone()

        if contact:
            print("Contact found:")
            print(contact)
        else:
            print("Contact not found.")

        cursor.close()
        connection.close()
while True:
    print("---Sanzhar Phonebook v1.0---")
    print("1.Create table")
    print("2.Add Number and Name")
    print("3.Delete contact")
    print("4.Exit")
    print("5.Update contact")
    print("6.Find contact")
    print("7.Insert CSV")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_table()
        print("You created a table")
    elif choice == "2":
        add_information()
        print("You added a number")
    elif choice == "3":
        delete_contact()
        print("You deleted a contact")
    elif choice == "4":
        break
    elif choice == "5":
        update_contact()
        print("You updated a contact")
    elif choice == "6":
        find_contact()
        print("You found a contact")
    elif choice == "7":
        insert_from_csv()