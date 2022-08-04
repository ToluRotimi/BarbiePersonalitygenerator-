from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,IntegerField,DateField
from datetime import date
from wtforms.validators import DataRequired, Length,ValidationError


class checkChoicesAreNotNone():
    def __init__(self, message):
        self.message = message
    
    def __call__(self,form,field):
        if field.data == None:
            raise ValidationError(self.message)
          
class usersForm(FlaskForm):
    forename = StringField('Enter Forename',validators=[DataRequired(), Length(min=1, max=50)])
    surname = StringField('Enter Surname',validators=[DataRequired(), Length(min=1, max=50)])
    dob= DateField('Date of Birth')
    submit=SubmitField('Submit')

class barbie_eraForm(FlaskForm):
    era_decade = SelectField('Barbie Decade',choices=[("2000's","2000's"),("1990's","1990's"),("1980's","1980's"),("1970's","1970's"),("1960's","1960's"),("1950's","1950's")],validators=[DataRequired(),checkChoicesAreNotNone('Please pick a date')])
    submit = SubmitField('Submit')

class user_eraForm(FlaskForm):
    user_id = StringField('User Name')
    era_id = StringField('What year was the barbie character released?')
    user_era_decade=SelectField('Birth-Year of User', choices=[("2000's","2000's"),("1990's","1990's"),("1980's","1980's"),("1970's","1970's"),("1960's","1960's"),("1950's","1950's")],validators=[DataRequired(),checkChoicesAreNotNone('Please pick a date')])
    submit = SubmitField('Submit')
