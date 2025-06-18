from flask import Flask, render_template, request
from bot import get_response  # Make sure bot.py has this function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = get_response(user_input)
    return render_template("index.html", bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
