from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keepitsecret"

@app.route("/")
def index():
    if "surveyors" not in session:
        session["surveyors"] = []
    return render_template("index.html")

@app.route("/submission", methods=["POST"])
def submission():
    temp_user = {
        "name" : request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"]
    }
    session["surveyors"].append(temp_user)
    return redirect("/results.html")

@app.route("/results")
def results_page():
    return render_template("results.html", surveyors=session["surveyors"])


if __name__ == "__main__":
    app.run(debug=True)