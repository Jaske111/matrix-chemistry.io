from flask import Flask, render_template, request
from datetime import date
from matrix import calculate_matrix

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        birthdate = request.form.get("birthdate", "").strip()
        try:
            if not name or len(name) > 50:
                raise ValueError("Укажи имя длиной от 1 до 50 символов.")
            born = date.fromisoformat(birthdate)
            if born > date.today():
                raise ValueError("Дата рождения не может быть в будущем.")
            result = calculate_matrix(name, born)
        except (ValueError, TypeError):
            error = "Проверь имя и дату рождения. Дата должна быть корректной и не из будущего."
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
