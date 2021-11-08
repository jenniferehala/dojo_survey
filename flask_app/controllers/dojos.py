from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate", methods=["POST"])
def validate_dojo():
    if Dojo.validate_dojo(request.form):
        print("Made it")
        data = {
            "name": request.form["name"],
            "location": request.form["location"],
            "language": request.form["language"],
            "comment": request.form["comment"]
        }
        id = Dojo.save(data)
        return redirect(f"/results/{id}")
    else:
        return redirect("/")

@app.route("/results/<int:id>")
def results_page(id):
    data = {
        "id": id
    }
    dojo = Dojo.results(data)
    return render_template("results.html", dojo=dojo)


if __name__ == "__main__":
    app.run(debug=True)