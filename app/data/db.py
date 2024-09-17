import sqlite3


def get_employees() -> list:
    data = []

    try:
        sql_con = sqlite3.connect("employees.db")
        cursor = sql_con.cursor()

        query = "SELECT * FROM Employees"

        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print(f"{error = }")

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою даних успішно завершена")

        return data


def insert_data(
    first_name: str,
    last_name: str,
    age: int|None = None,
    position: str|None = None,
    salary: float|None = None
    ) -> None:

    try:
        sql_con = sqlite3.connect("employees.db")
        cursor = sql_con.cursor()

        query = "INSERT INTO Employees (first_name, last_name, age, position, salary) VALUES (?, ?, ?, ?, ?)"
        data = (first_name, last_name, age, position, salary)

        cursor.execute(query, data)
        sql_con.commit()
        cursor.close()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print(f"{error = }")

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою даних успішно завершена")
