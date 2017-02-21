from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,PasswordField
from wtforms.validators import InputRequired

class clientForm(FlaskForm):
    cfname= StringField('First Name', validators=[InputRequired()])
    clname= StringField('Last Name', validators=[InputRequired()])
    ccontact= IntegerField('contact',validators=[InputRequired()])
    cemail= StringField('E-mail',validators=[InputRequired()])
    cpassword= PasswordField('Password',validators=[InputRequired()])
    cadd1=StringField('Address 1', validators=[InputRequired()])
    cadd2=StringField('Address 2', validators=[InputRequired()])
    ccity= StringField('City', validators=[InputRequired()])
    cparish= StringField('Parish', validators=[InputRequired()])

class driverForm(FlaskForm):
    dfname= StringField('First Name', validators=[InputRequired()])
    dlname= StringField('Last Name', validators=[InputRequired()])
    dcontact= IntegerField('Contact',validators=[InputRequired()])
    demail= StringField('E-mail',validators=[InputRequired()])
    dpassword= PasswordField('Password',validators=[InputRequired()])
    dadd1=StringField('Address 1', validators=[InputRequired()])
    dadd2=StringField('Address 2', validators=[InputRequired()])
    dcity= StringField('City', validators=[InputRequired()])
    dparish= StringField('Parish', validators=[InputRequired()])
    dtrn=IntegerField('TRN',validators=[InputRequired()])

class operatorForm(FlaskForm):
    ofname= StringField('First Name', validators=[InputRequired()])
    olname= StringField('Last Name', validators=[InputRequired()])
    oadd1=StringField('Address 1', validators=[InputRequired()])
    oadd2=StringField('Address 2', validators=[InputRequired()])
    ocity= StringField('City', validators=[InputRequired()])
    oparish= StringField('Parish', validators=[InputRequired()])
    otrn=IntegerField('TRN',validators=[InputRequired()])

class vehicleForm(FlaskForm):
    platenum= StringField('Registration Number', validators=[InputRequired()])
    vmodel= StringField('Model',validators=[InputRequired()])
    vmodel= StringField('Model',validators=[InputRequired()])
    vmake= StringField('Make',validators=[InputRequired()])
    vcolour= StringField('Colour',validators=[InputRequired()])
    seat_cap= StringField('Seating Capacity',validators=[InputRequired()])
    vclass= StringField('Class',validators=[InputRequired()])
