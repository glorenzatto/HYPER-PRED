from flask import Flask, render_template, request, redirect, session
from static.python.hypertension_prediction import HypertensionPredictionModel as hpm

app = Flask(__name__, static_folder="static")
app.config["SECRET_KEY"] = 'demoTCC'

def clean_session():
    session.pop("NAME", None)
    session.pop("GENDER", None)
    session.pop("AGE", None)
    session.pop("RACE", None)

@app.route("/")
def home():
    clean_session()

    return render_template("html/home.html")


@app.route("/input-basic-data")
def input_basic_data():

    return render_template("html/input_basic_data.html")


@app.route("/save-basic-data", methods=["POST"])
def save_basic_data():
    session["NAME"] = request.form.get("name")
    session["GENDER"] = request.form.get("gender")
    session["AGE"] = request.form.get("age")
    session["RACE"] = request.form.get("race")

    return redirect("/show-risk")


@app.route("/show-risk")
def render_results_page():

    data={
        'name': session["NAME"],
        'age': session["AGE"],
        'gender': session["GENDER"],
        'race': session["RACE"],
        'color' : '',
        'risk_percentage': ''
    }

    risk, color = hpm("input_dataset.xlsx").get_risk_percentage_and_color(data['age'], data['gender'], data['race'])

    data['risk_percentage'] = risk
    data['color'] = color

    return render_template("html/show_risk.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
