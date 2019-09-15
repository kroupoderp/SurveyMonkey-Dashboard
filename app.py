from flask import Flask, render_template
import fetch

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("home.html", surveys=fetch.getSurveys())