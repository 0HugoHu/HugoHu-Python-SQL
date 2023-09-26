import pytest
import sqlite3
from ids706_python_template.cli import (
    create_db,
    insert_db,
    retrieve_db,
    retrieve_db2,
    drop_table,
    update_db,
)


# Use an in-memory SQLite database for testing
@pytest.fixture
def setup_database():
    conn = create_db()
    yield conn
    conn.close()


def test_create_db(setup_database):
    # Check if the "employees" table was created
    cursor = setup_database.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='employees';"
    )
    result = cursor.fetchone()
    assert result is not None
    assert result[0] == "employees"


def test_insert_db(setup_database):
    insert_db(setup_database)
    cursor = setup_database.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    assert len(rows) == 3  # Check if all 3 records were inserted


def test_retrieve_db(setup_database, capsys):
    insert_db(setup_database)
    retrieve_db(setup_database)
    captured = capsys.readouterr()
    expected_output = "Records inserted\n(1, 'John Doe', 'HR')\n(2, 'Jane Smith', 'Finance')\n(3, 'Bob Johnson', 'IT')\nRecords retrieved\n"
    assert captured.out.strip() == expected_output.strip()


def test_retrieve_db2(setup_database, capsys):
    insert_db(setup_database)
    retrieve_db2(setup_database)
    captured = capsys.readouterr()
    expected_output = (
        "Records inserted\n(1, 'John Doe', 'HR')\nRecords retrieved\n"
    )
    assert captured.out.strip() == expected_output.strip()


def test_update_db(setup_database):
    insert_db(setup_database)
    update_db(setup_database)
    cursor = setup_database.cursor()
    cursor.execute(
        "SELECT * FROM employees WHERE name = 'Jane Smith' AND department = 'HR'"
    )
    rows = cursor.fetchall()
    assert len(rows) == 1  # Check if only 1 record was updated


def test_drop_table(setup_database):
    insert_db(setup_database)
    drop_table()
    cursor = setup_database.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='employees';"
    )
    result = cursor.fetchone()
    assert result is None
