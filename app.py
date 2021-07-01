from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def root():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/diys')
def diys():
    return render_template("diys.html")

@app.route('/art')
def art():
    return render_template("art.html")

@app.route('/bugs')
def bugs():
    return render_template("bugs.html")

@app.route('/fish')
def fish():
    return render_template("fish.html")

@app.route('/seacreatures')
def seacreatures():
    return render_template("seacreatures.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))     
    app.run(port=port, debug=True)
