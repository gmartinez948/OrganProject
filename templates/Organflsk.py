'''
Flask server calling the html code
'''

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    images = {
        "top": "https://ufhealth.org/sites/default/files/media/social-media/2020-April-NDLM-2020-Organ-Donation.png",
        "middle": "https://lh3.googleusercontent.com/pw/ACtC-3flTYKdLYvr69_zSZyYBqDcI8DdoKnvVBcXqfS66akpOknrsl-io2AWviWBjdrcVDxOIsGuTog2oBteUJfTN94bG8Y07KH97p9HooB32v_lgxyPtYYJbO9i6Jb-vtMU_xTVPL5pOjhA8aPDTErlKVE=w388-h335-no?authuser=0",
    }
    return render_template("index1.html", images=images, title="some title")

if __name__ == '__main__':
    app.run()


