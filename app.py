from utils import *
from build_queries import *
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import select
from flask_migrate import Migrate
from models import *
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('URI')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def root():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/diys', methods=['GET', 'POST'])
def diys():
    if request.method == 'POST':

        # Get filter parameters
        data =  {
            'filter_diys': request.form.get('filter_diys'),
            'filter_collect': request.form.get('filter_collect'),
            'sort': request.form.get('sort')
        }

        # Building the query
        query = select_diys(data)

        # Execute query
        result = db.session.execute(query)

        return render_template("diys.html", filter_data=result)
    else:
        return render_template("diys.html")

@app.route('/add_diys', methods=['GET', 'POST'])
def add_diys():
    return render_template("/add/add_diy.html")

@app.route('/search_diys', methods=['GET', 'POST'])
def search_diys():
    if request.method == 'POST':

        # Get search parameters
        data =  {
            'search_diys': request.form.get('search_diys'),
        }

        # Building the query
        query = select_diy_name(data)

        # Execute query
        result = db.session.execute(query)

        return render_template("/search/search_diys.html", search_data=result)
    else:
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
    if request.method == 'POST':

        # Get filter parameters
        data =  {
            'filter_bugs': request.form.get('filter_bugs'),
            'filter_collect': request.form.get('filter_collect'),
            'sort': request.form.get('sort')
        }

        # Building the query
        query = select_bugs(data)

        # Execute query
        result = db.session.execute(query)

        # Save date & time results into readable format
        rows = convert_rows(result)
            
        return render_template("bugs.html", filter_data=rows)
    else:
        return render_template("bugs.html")

@app.route('/add_bugs', methods=['GET', 'POST'])
def add_bugs():
    return render_template("/add/add_bugs.html")

@app.route('/fish', methods=['GET', 'POST'])
def fish():
    if request.method == 'POST':

        # Get filter parameters
        data =  {
            'filter_fish': request.form.get('filter_fish'),
            'filter_collect': request.form.get('filter_collect'),
            'sort': request.form.get('sort')
        }

        # Building the query
        query = select_fish(data)

        # Execute query
        result = db.session.execute(query)

        # Save date & time results into readable format
        rows = convert_rows(result)
            
        return render_template("fish.html", filter_data=rows)
    else:
        return render_template("fish.html")

@app.route('/add_fish', methods=['GET', 'POST'])
def add_fish():
    return render_template("/add/add_fish.html")

@app.route('/seacreatures', methods=['GET', 'POST'])
def seacreatures():
    if request.method == 'POST':

        # Get filter parameters
        data =  {
            'filter_sea_creatures': request.form.get('filter_sea_creatures'),
            'filter_collect': request.form.get('filter_collect'),
            'sort': request.form.get('sort')
        }

        # Building the query
        query = select_sea_creatures(data)

        # Execute query
        result = db.session.execute(query)

        # Save date & time results into readable format
        rows = convert_rows(result)
            
        return render_template("seacreatures.html", filter_data=rows)
    else:
        return render_template("seacreatures.html")

@app.route('/add_seacreatures', methods=['GET', 'POST'])
def add_seacreatures():
    return render_template("/add/add_seacreatures.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("/error/404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("/error/500.html"), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))     
    app.run(port=port, debug=True)
