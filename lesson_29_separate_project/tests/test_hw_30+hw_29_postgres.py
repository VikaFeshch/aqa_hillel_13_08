import psycopg2
import pytest
import allure

def get_db_connection():
    return psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="localhost",
        port="5433"
    )

@allure.epic("DataBase Epic")
@allure.feature("Connections Feature")
def test_database_connection():
    with allure.step("Connection"):
        conn = get_db_connection()
    with allure.step("Assert"):
        assert conn is not None

@allure.epic("DataBase Epic")
@allure.feature("Insert Feature")
def test_data_insertion():
    with allure.step("Connection"):
        conn = get_db_connection()
        cursor = conn.cursor()
    with allure.step("Insert"):
        cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE id=1")
        result = cursor.fetchone()
    with allure.step("Assert"):
        assert result[1] == 'John'

@allure.epic("DataBase Epic")
def fetch_users():
    with allure.step("Connection"):
        conn = get_db_connection()
        cursor = conn.cursor()
    with allure.step("Fetch"):
        try:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            assert len(rows) > 0, "No users found in the database"
            return rows
        except Exception as e:
            pytest.fail(f"Error during data fetch: {e}")
        finally:
            cursor.close()
            conn.close()

@allure.epic("DataBase Epic")
@allure.feature("Fetch Feature")
def test_fetch_users():
    users = fetch_users()
    with allure.step("Assert"):
        assert len(users) > 0, "No users found"
        for user in users:
            assert len(user) == 2, "User data should have 2 columns (id and name)"
            assert isinstance(user[0], int), "User ID should be an integer"
            assert isinstance(user[1], str), "User name should be a string"

@allure.epic("DataBase Epic")
@allure.feature("Update Feature")
def test_update_data():
    with allure.step("Connection"):
        conn = get_db_connection()
        cursor = conn.cursor()
    with allure.step("Update"):
        cursor.execute("UPDATE users SET name='Jane' WHERE id=1")
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE id=1")
        result = cursor.fetchone()

    with allure.step("Assert"):
        assert result is not None and result[1] == 'Jane'

@allure.epic("DataBase Epic")
@allure.feature("Delete Feature")
def test_delete_data():
    with allure.step("Connection"):
        conn = get_db_connection()
        cursor = conn.cursor()
    with allure.step("Delete"):
        cursor.execute("DELETE FROM users WHERE id=1")
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE id=1")
        result = cursor.fetchone()

    with allure.step("Assert"):
        assert result is None

if __name__ == "__main__":
    test_database_connection()
    test_data_insertion()
    fetch_users()
    test_update_data()
    test_delete_data()

