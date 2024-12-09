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
        assert conn is not None

@allure.epic("DataBase Epic")
@allure.feature("Insert Feature")
@pytest.mark.parametrize("user_id, user_name", [
    (1, "John"),
    (2, "Jane"),
    (3, "Alice"),
])
def test_data_insertion(user_id, user_name):
    with allure.step("Insert Data"):
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (user_id, user_name))
                conn.commit()
                cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
                result = cursor.fetchone()
                assert result[1] == user_name

@allure.epic("DataBase Epic")
@allure.feature("Fetch Feature")
def test_fetch_users():
    with allure.step("Fetch Data"):
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                rows = cursor.fetchall()
                assert len(rows) > 0, "No users found"
                for user in rows:
                    assert len(user) == 2
                    assert isinstance(user[0], int)
                    assert isinstance(user[1], str)
