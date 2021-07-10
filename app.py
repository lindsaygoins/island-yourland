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

@app.route('/add_diys')
def add_diys():
    return render_template("add_diy.html")

@app.route('/art')
def art():
    return render_template("art.html")

@app.route('/add_art')
def add_art():
    return render_template("add_art.html")

@app.route('/bugs')
def bugs():
    return render_template("bugs.html")

@app.route('/fish')
def fish():
    return render_template("fish.html")

@app.route('/seacreatures')
def seacreatures():
    return render_template("seacreatures.html")

@app.route('/flowers')
def flowers():
    return render_template("flowers.html")

@app.route('/items')
def items():
    return render_template("items.html")

@app.route('/add_items', methods=['GET', 'POST'])
def add_items():
    return render_template("add_items.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))     
    app.run(port=port, debug=True)
