from flask import Flask, render_template
from datetime import date
from apiii import get_params

app = Flask(__name__)

@app.route("/")
def home():
    current_date = date.today()
    current_year = current_date.year
    return render_template('index.html', year=current_year)

@app.route("/guess/<nameuser>")
def guess(nameuser):
    name = nameuser
    params = get_params(name)
    age = params[0]['age']
    gender = params[1]['gender']
    return render_template('guess.html', name=name, age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)

