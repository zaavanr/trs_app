from app import app
from flask import render_template, request, redirect, url_for, jsonify

@app.route('/')
def home():
    return render_template('map.html', x=12)


@app.route('/save-coord', methods=['GET', 'POST'])
def save_coord():
    x = request.form['x']
    y = request.form['y']
    return jsonify(xcoord=x,ycoord=y)
