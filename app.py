from flask import Flask, render_template
import fetch

app = Flask(__name__)

surveys = fetch.getSurveys()

@app.route("/")
def present():
    return render_template("home.html", surveys=surveys)

@app.route("/results/test")
def survey_one():
    return fetch.getResults("188745355")

@app.route("/results/Trends in software development")
def survey_two():
    return fetch.getResults("188231210")

@app.route("/results/Canadian vacation preferences")
def survey_three():
    return fetch.getResults("167439285")

@app.route("/results/Geography quiz")
def survey_four():
    return fetch.getResults("188308498")