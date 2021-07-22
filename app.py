from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def root():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/diys', methods=['GET', 'POST'])
def diys():
    return render_template("diys.html")

@app.route('/add_diys', methods=['GET', 'POST'])
def add_diys():
    return render_template("/add/add_diy.html")

@app.route('/search_diys', methods=['GET', 'POST'])
def search_diys():
    return render_template("/search/search_diys.html")

@app.route('/art', methods=['GET', 'POST'])
def art():
    return render_template("art.html")

@app.route('/add_art', methods=['GET', 'POST'])
def add_art():
    return render_template("/add/add_art.html")

@app.route('/search_art', methods=['GET', 'POST'])
def search_art():
    return render_template("/search/search_art.html")

@app.route('/items', methods=['GET', 'POST'])
def items():
    return render_template("items.html")

@app.route('/add_items', methods=['GET', 'POST'])
def add_items():
    return render_template("/add/add_items.html")

@app.route('/search_items', methods=['GET', 'POST'])
def search_items():
    return render_template("/search/search_items.html")

@app.route('/flowers', methods=['GET', 'POST'])
def flowers():
    return render_template("flowers.html")

@app.route('/add_flowers', methods=['GET', 'POST'])
def add_flowers():
    return render_template("/add/add_flowers.html")

@app.route('/bugs', methods=['GET', 'POST'])
def bugs():
    return render_template("bugs.html")

@app.route('/add_bugs', methods=['GET', 'POST'])
def add_bugs():
    return render_template("/add/add_bugs.html")

@app.route('/fish', methods=['GET', 'POST'])
def fish():
    return render_template("fish.html")

@app.route('/add_fish', methods=['GET', 'POST'])
def add_fish():
    return render_template("/add/add_fish.html")

@app.route('/seacreatures', methods=['GET', 'POST'])
def seacreatures():
    return render_template("seacreatures.html")

@app.route('/add_seacreatures', methods=['GET', 'POST'])
def add_seacreatures():
    return render_template("/add/add_seacreatures.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))     
    app.run(port=port, debug=True)
