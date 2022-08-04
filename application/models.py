from application import db

#creating schema called users 
class user(db.Model): 
    user_id=db.Column(db.Integer, primary_key=True)
    forename=db.Column(db.String(50), nullable = False)
    surname=db.Column(db.String(50), nullable = False)
    dob=db.Column(db.Date, nullable = False)
    user_era= db.relationship('user_era', backref='user')
    def __str__(self):
        return f"{self.forename},{self.surname},{self.dob}"

#creates schema called barbie_era         
class barbie_era(db.Model):
    era_id = db.Column(db.Integer, primary_key=True)
    era_decade = db.Column(db.Integer, nullable = False)
    user_era= db.relationship('user_era', backref='barbie_era')
    def __str__(self):
        return f"{self.era_decade}"

class user_era(db.Model):
    user_era_id = db.Column(db.Integer, primary_key =True)
    user_era_decade = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    era_id = db.Column(db.Integer, db.ForeignKey('barbie_era.era_id'))
    def __str__(self):
        return f"{self.user_era_decade}"
