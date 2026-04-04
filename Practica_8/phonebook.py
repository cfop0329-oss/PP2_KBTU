import csv
from connect import get_connection


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name TEXT,
            number TEXT
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def add_information():
    name = input("Enter name: ")
    number = input("Enter number: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s, %s)", (name, number))

    conn.commit()
    cur.close()
    conn.close()


def delete_contact():
    name = input("Enter name to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (name,))

    conn.commit()
    cur.close()
    conn.close()

def show_all_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_all_contacts()")
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()

def find_contact():
    pattern = input("Search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


def insert_from_csv():
    filename = input("Enter CSV file: ")

    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            name, number = row
            cur.execute("CALL upsert_user(%s, %s)", (name, number))

    conn.commit()
    cur.close()
    conn.close()


def update_contact():
    name = input("Enter name: ")
    number = input("Enter new number: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s, %s)", (name, number))

    conn.commit()
    cur.close()
    conn.close()


while True:
    print("\n---Sanzhar Phonebook v1.0---")
    print("1.Create table")
    print("2.Add Number and Name")
    print("3.Delete contact")
    print("4.Exit")
    print("5.Update contact")
    print("6.Find contact")
    print("7.Insert CSV")
    print("8.Show all contacts")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_table()
        print("Table created")

    elif choice == "2":
        add_information()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        break

    elif choice == "5":
        update_contact()

    elif choice == "6":
        find_contact()

    elif choice == "7":
        insert_from_csv()

    elif choice == "8":
        show_all_contacts()

    else:
        print("Invalid choice")