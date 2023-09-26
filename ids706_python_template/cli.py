"""CLI interface for ids706_python_template project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

import sqlite3


def drop_table():
    """
    Drop the table if it exists
    return: None
    """
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    cursor.execute(
        "DROP TABLE IF EXISTS employees"
    )  # Drop the "employees" table if it exists
    conn.commit()
    conn.close()
    print("Table dropped")


def create_db():
    """
    Create a database if not exists
    return: connection object
    """
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS employees
                      (id INTEGER PRIMARY KEY,
                       name TEXT,
                       department TEXT)"""
    )
    conn.commit()
    print("Table created")
    return conn


def insert_db(conn):
    """
    Insert records into the database
    return: None
    """
    # List of records to insert
    employee_data = [
        ("John Doe", "HR"),
        ("Jane Smith", "Finance"),
        ("Bob Johnson", "IT"),
    ]

    cursor = conn.cursor()
    # Insert multiple records
    for employee in employee_data:
        cursor.execute(
            "INSERT INTO employees (name, department) VALUES (?, ?)", employee
        )

    print("Records inserted")
    conn.commit()


def update_db(conn):
    """
    Update records in the database
    return: None
    """
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE employees SET department = 'HR' WHERE name = 'Jane Smith'"
    )
    conn.commit()
    print("Records updated")


def retrieve_db(conn):
    """
    Retrieve all records from the database
    return: None
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print("Records retrieved")


def retrieve_db2(conn):
    """
    Retrieve HR records from the database
    return: None
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE department = 'HR'")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print("Records retrieved")


def main():  # pragma: no cover
    drop_table()
    conn = create_db()
    insert_db(conn)
    retrieve_db(conn)
    update_db(conn)
    retrieve_db(conn)
    retrieve_db2(conn)
    conn.close()
