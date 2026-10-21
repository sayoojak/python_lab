
from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# Store the database outside OneDrive
DB_FOLDER = r"C:\FlaskStudent"
os.makedirs(DB_FOLDER, exist_ok=True)
DB_PATH = os.path.join(DB_FOLDER, "students.db")


def get_db():
    return sqlite3.connect(DB_PATH)


# Create the database table
with get_db() as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age_text = request.form.get("age", "").strip()

        try:
            age = int(age_text)

            if not name or age < 1:
                raise ValueError

            with get_db() as con:
                con.execute(
                    "INSERT INTO students (name, age) VALUES (?, ?)",
                    (name, age)
                )

            message = "Student saved successfully!"

        except ValueError:
            message = "Enter a valid name and age."

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Registration</title>
    </head>
    <body>
        <h2>Student Registration</h2>
        <p>""" + message + """</p>

        <form method="POST">
            Name:
            <input type="text" name="name" required>
            <br><br>

            Age:
            <input type="number" name="age" min="1" required>
            <br><br>

            <input type="submit" value="Register">
        </form>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
