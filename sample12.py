
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "")
        return f"Welcome, {name}!"

    return """
    <h2>Student Form</h2>
    <form method="POST">
        Name: <input type="text" name="name" required>
        <input type="submit" value="Submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
