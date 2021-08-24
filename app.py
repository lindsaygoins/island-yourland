from utils import *
from build_queries import *
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import select
from flask_migrate import Migrate
from models import *
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
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
    if request.method == 'POST':

        # Get update parameters
        data =  {
            'diy_name': request.form.get('diy_name'),
            'diy_user': request.form.get('diy_user')
        }

        # Build & execute the query to check if DIY exists
        query = select_diy_name(data)
        result = db.session.execute(query)
        row = result.first()

        # If DIY exists, build & execute the UPDATE query
        if not row:
            # Add error message here!
            print("Not in db")
        else:
            data['diy_id'] = row[0].diyid
            query = update_diy(data)
            db.session.execute(query)
            db.session.commit()

        return redirect(url_for('diys'))
    else:
        return render_template("/add/add_diy.html")

@app.route('/search_diys', methods=['GET', 'POST'])
def search_diys():
    if request.method == 'POST':

        # Get search parameters
        data =  {
            'diy_name': request.form.get('search_diys'),
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
    if request.method == 'POST':

        # Get filter parameters
        data =  {
            'filter_art': request.form.get('filter_art'),
            'filter_collect': request.form.get('filter_collect'),
            'sort': request.form.get('sort')
        }

        # Building the query
        query = select_art(data)

        # Execute query
        result = db.session.execute(query)
        
        return render_template("art.html", filter_data=result)
    else:
        return render_template("art.html")

@app.route('/add_art', methods=['GET', 'POST'])
def add_art():
    if request.method == 'POST':

        # Get update parameters
        data =  {
            'art_name': request.form.get('art_name'),
            'art_user': request.form.get('art_user')
        }

        # Build & execute the query to check if Artwork exists
        query = select_art_name(data)
        result = db.session.execute(query)
        row = result.first()

        # If Artwork exists, build & execute the UPDATE query
        if not row:
            # Add error message here!
            print("Not in db")
        else:
            data['art_id'] = row[0].artid
            query = update_art(data)
            db.session.execute(query)
            db.session.commit()

        return redirect(url_for('art'))
    else:
        return render_template("/add/add_art.html")

@app.route('/search_art', methods=['GET', 'POST'])
def search_art():
    if request.method == 'POST':

        # Get search parameters
        data =  {
            'art_name': request.form.get('search_art'),
        }

        # Building the query
        query = select_art_name(data)

        # Execute query
        result = db.session.execute(query)

        return render_template("/search/search_art.html", search_data=result)
    else:
        return render_template("/search/search_art.html")

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':

        # Get filter parameters
        data =  {
            'filter_items': request.form.get('filter_items'),
            'filter_collect': request.form.get('filter_collect'),
            'sort': request.form.get('sort')
        }

        # Building the query
        query = select_items(data)

        # Execute query
        result = db.session.execute(query)
        
        return render_template("items.html", filter_data=result)
    else:
        return render_template("items.html")

@app.route('/add_items', methods=['GET', 'POST'])
def add_items():
    if request.method == 'POST':

        # Get update parameters
        data =  {
            'item_name': request.form.get('item_name'),
            'item_user': request.form.get('item_user')
        }

        # Build & execute the query to check if item exists
        query = select_item_name(data)
        result = db.session.execute(query)
        row = result.first()

        # If item exists, build & execute the UPDATE query
        if not row:
            # Add error message here!
            print("Not in db")
        else:
            data['item_id'] = row[0].itemid
            query = update_item(data)
            db.session.execute(query)
            db.session.commit()

        return redirect(url_for('items'))
    else:
        return render_template("/add/add_items.html")

@app.route('/search_items', methods=['GET', 'POST'])
def search_items():
    if request.method == 'POST':

        # Get search parameters
        data =  {
            'item_name': request.form.get('search_items'),
        }

        # Building the query
        query = select_item_name(data)

        # Execute query
        result = db.session.execute(query)

        return render_template("/search/search_items.html", search_data=result)
    else:
        return render_template("/search/search_items.html")

@app.route('/flowers', methods=['GET', 'POST'])
def flowers():
    if request.method == 'POST':

        # Get filter parameters
        data =  {
            'filter_flowers': request.form.get('filter_flowers'),
            'filter_collect': request.form.get('filter_collect'),
            'sort': request.form.get('sort')
        }

        # Building the query
        query = select_flowers(data)

        # Execute query
        result = db.session.execute(query)
        
        return render_template("flowers.html", filter_data=result)
    else:
        return render_template("flowers.html")

@app.route('/add_flowers', methods=['GET', 'POST'])
def add_flowers():
    if request.method == 'POST':

        # Get update parameters
        data =  {
            'flower_name': request.form.get('flower_name'),
        }

        # Build & execute query
        query = update_flowers(data)
        db.session.execute(query)
        db.session.commit()

        return redirect(url_for('flowers'))

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
    if request.method == 'POST':

        # Get update parameters
        data =  {
            'bug_name': request.form.get('bug_name'),
        }

        # Build & execute query
        query = update_bug(data)
        db.session.execute(query)
        db.session.commit()

        return redirect(url_for('bugs'))

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
    if request.method == 'POST':

        # Get update parameters
        data =  {
            'fish_name': request.form.get('fish_name'),
        }

        # Build & execute query
        query = update_fish(data)
        db.session.execute(query)
        db.session.commit()

        return redirect(url_for('fish'))

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
    if request.method == 'POST':

        # Get update parameters
        data =  {
            'sea_creature_name': request.form.get('sea_creature_name'),
        }

        # Build & execute query
        query = update_sea_creatures(data)
        db.session.execute(query)
        db.session.commit()

        return redirect(url_for('seacreatures'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("/error/404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("/error/500.html"), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))     
    app.run(port=port, debug=True)
