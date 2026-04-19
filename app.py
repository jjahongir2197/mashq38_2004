from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/user33", methods=["GET", "POST"])
def user33():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")

        return render_template(
            "result33.html",
            username=username,
            email=email
        )

    return render_template("index33.html")
