from app import app
from flask import render_template

@app.route("/")
def index():
    colors = ['success', 'primary', 'secondary', 'warning', 'danger']
    return render_template('base.html', name = 'Brandon', colors = colors)

@app.route("/posts")
def posts():
    return "Brandon Posts"