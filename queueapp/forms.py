from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class Form(FlaskForm):
    student_name = StringField("Enter Your Name:")
    reason = SelectField("Select Reason: ", choices=[("Select", "Select"),("HW", "HW"), ("Concepts", "Concepts")])
    button = SubmitField("Submit")