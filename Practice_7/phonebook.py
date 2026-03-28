import csv
from connect import get_connection


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    );
    """
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.close()
        print("Table created successfully.")
    except Exception as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        if conn:
            conn.close()


def insert_from_console():
    first_name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    query = """
    INSERT INTO phonebook (first_name, phone)
    VALUES (%s, %s)
    ON CONFLICT (phone) DO NOTHING;
    """

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, (first_name, phone))
        conn.commit()
        cur.close()
        print("Contact added.")
    except Exception as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        if conn:
            conn.close()


def insert_from_csv(filename="contacts.csv"):
    query = """
    INSERT INTO phonebook (first_name, phone)
    VALUES (%s, %s)
    ON CONFLICT (phone) DO NOTHING;
    """

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        with open(filename, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cur.execute(query, (row["first_name"], row["phone"]))

        conn.commit()
        cur.close()
        print("CSV imported.")
    except Exception as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        if conn:
            conn.close()


def show_all_contacts():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, first_name, phone FROM phonebook ORDER BY id;")
        rows = cur.fetchall()

        if not rows:
            print("No contacts found.")
        else:
            for row in rows:
                print(row)

        cur.close()
    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            conn.close()


def search_by_name():
    name = input("Enter name: ").strip()

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, first_name, phone FROM phonebook WHERE first_name ILIKE %s;",
            (f"%{name}%",)
        )
        rows = cur.fetchall()

        if not rows:
            print("No matches.")
        else:
            for row in rows:
                print(row)

        cur.close()
    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            conn.close()


def search_by_phone_prefix():
    prefix = input("Enter phone prefix: ").strip()

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, first_name, phone FROM phonebook WHERE phone LIKE %s;",
            (f"{prefix}%",)
        )
        rows = cur.fetchall()

        if not rows:
            print("No matches.")
        else:
            for row in rows:
                print(row)

        cur.close()
    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            conn.close()


def update_contact():
    print("1. Update name by phone")
    print("2. Update phone by name")
    choice = input("Choose: ").strip()

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        if choice == "1":
            phone = input("Enter current phone: ").strip()
            new_name = input("Enter new name: ").strip()
            cur.execute(
                "UPDATE phonebook SET first_name = %s WHERE phone = %s;",
                (new_name, phone)
            )
        elif choice == "2":
            name = input("Enter current name: ").strip()
            new_phone = input("Enter new phone: ").strip()
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE first_name = %s;",
                (new_phone, name)
            )
        else:
            print("Invalid choice.")
            return

        conn.commit()
        print("Updated rows:", cur.rowcount)
        cur.close()
    except Exception as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        if conn:
            conn.close()


def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose: ").strip()

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        if choice == "1":
            name = input("Enter name: ").strip()
            cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (name,))
        elif choice == "2":
            phone = input("Enter phone: ").strip()
            cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
        else:
            print("Invalid choice.")
            return

        conn.commit()
        print("Deleted rows:", cur.rowcount)
        cur.close()
    except Exception as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        if conn:
            conn.close()


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Insert contact from console")
        print("3. Import contacts from CSV")
        print("4. Show all contacts")
        print("5. Search by name")
        print("6. Search by phone prefix")
        print("7. Update contact")
        print("8. Delete contact")
        print("9. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            insert_from_csv()
        elif choice == "4":
            show_all_contacts()
        elif choice == "5":
            search_by_name()
        elif choice == "6":
            search_by_phone_prefix()
        elif choice == "7":
            update_contact()
        elif choice == "8":
            delete_contact()
        elif choice == "9":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()