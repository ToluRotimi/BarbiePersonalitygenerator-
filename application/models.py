from application import db

# creating a schema for the barbie_era to calculate era the user was born 
# display the barbie era it corresponds to
class barbie_era(db.Model):
    barbie_era_id = db.Column(db.Integer, primary_key =True)
    barbie_year = db.Column(db.String(20), nullable = False)
    birth_year = db.Column(db.String(20), nullable = False)
    user= db.Column(db.Integer, db.ForeignKey('user.user_id'))
    def __str__(self):
        return f"{self.barbie_year},{self.birth_year}"

#creating schema called users 
class user(db.Model): 
    user_id=db.Column(db.Integer, primary_key=True)
    forename=db.Column(db.String(50), nullable = False)
    surname=db.Column(db.String(50), nullable = False)
    user_era=db.relationship('barbie_era', backref='users')
    def __str__(self):
        return f"{self.forename},{self.surname}"

class user_era(db.Model):
    user_era_id = db.Column(db.Integer, primary_key =True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    barbie_era_id = db.Column(db.Integer, db.ForeignKey('barbie_era.barbie_era_id'))