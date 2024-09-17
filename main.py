from flask import Flask, render_template, request, redirect

from app.data import db


app = Flask(__name__, static_folder="app/static", template_folder="app/templates")


@app.get("/")
def index():
    return render_template("index.html", title="Головна сторінка")


@app.get("/employees/")
def show_employees():
    employees = db.get_employees()
    pizza_name1 = employees[0]
    pizza_name2 = employees[1]
    context = {
        "title": "Список працівників",
        "employees": employees
    }
    return render_template("employees.html", **context)


@app.get("/add_employee/")
def add_employee():
    return render_template("add_employee.html", title="Додати нового працівника")


@app.post("/add_employee/")
def add_employee_post():
    data = request.form
    print(f"{data = }")
    db.insert_data(**data)
    return redirect("/employees/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
