from flask import Flask, render_template, request

import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def register():
    if (not request.form.get("name") or not request.form.get("feedback") or not request.form.get("email")):
        return render_template("form-err.html")

    with open("details.csv", "a+") as f:
        writer = csv.writer(f)
        # writes row in  the order Name,email,course,rating,feedback
        writer.writerow((request.form.get("name"), request.form.get("email"), request.form.get(
            "course"), request.form.get("rating"), request.form.get("feedback")))

    return render_template("registered.html")
