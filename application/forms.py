from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,IntegerField,DateField
from datetime import date
from wtforms.validators import DataRequired, Length,ValidationError

          
class usersForm(FlaskForm):
    forename = StringField('Enter Forename',validators=[DataRequired(), Length(min=1, max=50)])
    surname = StringField('Enter Surname',validators=[DataRequired(), Length(min=1, max=50)])
    submit=SubmitField('Submit')

class user_eraForm(FlaskForm):
    user_era = SelectField('User', choices=[])
    user_era_decade=SelectField('Birth-Year of User', choices=[("2000's","2000's"),("1990's","1990's"),("1980's","1980's"),("1970's","1970's"),("1960's","1960's"),("1950's","1950's")],validators=[DataRequired(),checkChoicesAreNotNone('Please pick a date')])
    submit = SubmitField('Submit')
