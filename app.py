from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_number():
    if request.method == "GET":
        return render_template("starting_page.html")
    else:
        min_number = int(request.form.get("min", 0))
        max_number = int(request.form.get("max", 1000))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you won":
            return render_template("endgame_form.html", guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return render_template("main_form.html", guess=guess, min=min_number, max=max_number)
