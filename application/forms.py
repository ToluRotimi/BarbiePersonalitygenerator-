from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired, Length

class usersForm(FlaskForm):
    forename = StringField('Enter Forename',validators=[DataRequired(), Length(min=1, max=50)])
    surname = StringField('Enter Surname',validators=[DataRequired(), Length(min=1, max=50)])
    submit=SubmitField('Submit')

class barbie_eraForm(FlaskForm):
    user= SelectField('User', choices=[])
    barbie_year=SelectField('Decade Barbie Character was released', choices=[("2000's","2000's"),("1990's","1990's"),("1980's","1980's"),("1970's","1970's"),("1960's","1960's"),("1950's","1950's")],validators=[DataRequired()])
    birth_year=SelectField('Birth Year Of User', choices=[("2000's","2000's"),("1990's","1990's"),("1980's","1980's"),("1970's","1970's"),("1960's","1960's"),("1950's","1950's")],validators=[DataRequired()])
    submit = SubmitField('Submit')