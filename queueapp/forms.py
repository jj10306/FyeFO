from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class Form(FlaskForm):
    student_name = StringField("Enter your name")
    reason = SelectField("Reason", choices=[("HW", "HW"), ("Concepts", "Concepts")])
    button = SubmitField("Submit")