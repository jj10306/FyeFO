from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Form(FlaskForm):
    gtid = StringField("Scan you Buzzcard or type your GTID (9-digit number) below!")
    submit = SubmitField("Submit")