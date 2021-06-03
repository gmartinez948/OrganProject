'''
Flask server calling the html code
* Add redirect to home page
'''

from flask import Flask, render_template, redirect



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/About_us.html")
def about_us():
    return render_template("About_us.html")


@app.route("/Resources.html")
def resources():
    return render_template("Resources.html")

@app.route("/Research.html")
def research():
    return render_template("Research.html")


if __name__ == '__main__':
    app.run(debug = True)


