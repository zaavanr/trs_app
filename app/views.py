from app import app,db
from flask import render_template, request, redirect, url_for, jsonify,flash
from forms import clientForm, driverForm, operatorForm, vehicleForm
from models import Client, Driver, Operator, Vehicle

@app.route('/')

def home():
    return render_template('map.html', x=12)


@app.route('/save-coord', methods=['GET', 'POST'])
def save_coord():
    x = request.form['x']
    y = request.form['y']
    return jsonify(xcoord=x,ycoord=y)

@app.route('/add-client', methods=['POST','GET'])
def add_client():
    cform=clientForm()

    if request.method=='POST':
        if cform.validate_on_submit():
            cfname=cform.cfname.data
            clname=cform.clname.data
            ccontact=cform.ccontact.data
            cemail=cform.cemail.data
            cpassword=cform.cpassword.data
            cadd1=cform.cadd1.data
            cadd2=cform.cadd2.data
            cstreet=cform.cstreet.data
            ccity=cform.ccity.data
            cparish=cform.cparish.data

            client= Client(cfname,clname,ccontact,cemail,cpassword,cadd1,cadd2,cstreet,ccity,cparish)
            db.session.add(client)
            db.session.commit()

            flash('User added sucessfully','success')
            return redirect (url_for('home'))
    flash_errors(cform)
    return render_template('add_client.html',form=cform)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
