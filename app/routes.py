from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template('base.html')

@app.route("/favourites")
def favourites():
    colors = ['success', 'primary', 'secondary', 'warning', 'danger']
    return render_template('favourites.html', name = 'Brandon', colors = colors)