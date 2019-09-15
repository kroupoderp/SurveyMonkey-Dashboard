from flask import Flask, render_template
import fetch

app = Flask(__name__)

surveys = fetch.getSurveys()

@app.route("/")
def hello():
    return render_template("home.html", surveys=fetch.getSurveys())

@app.route("/results/Trends in software development")
def survey_one():
    return render_template("results.html", surveys=fetch.getSurveys(), questions=fetch.getQuestions("188231210"))

@app.route("/results/Canadian vacation preferences")
def survey_two():
    return render_template("results.html", surveys=fetch.getSurveys(), questions=fetch.getQuestions("167439285"))

@app.route("/results/Geography quiz")
def survey_three():
    return render_template("results.html", surveys=fetch.getSurveys(), questions=fetch.getQuestions("188308498")) 
