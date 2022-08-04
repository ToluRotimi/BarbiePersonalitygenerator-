from application import db

#creating schema called users 
class user(db.Model): 
    user_id=db.Column(db.Integer, primary_key=True)
    forename=db.Column(db.String(50), nullable = False)
    surname=db.Column(db.String(50), nullable = False)
    era=db.Column(db.Integer, db.ForeignKey('user_era.user_era_id'))
    def __str__(self):
        return f"{self.forename},{self.surname},{self.dob}"

# creating a schema for the user_era to calculate era the user was born
class user_era(db.Model):
    user_era_id = db.Column(db.Integer, primary_key =True)
    user_era_decade = db.Column(db.Integer, nullable = False)
    user_era = db.relationship('user', backref='user_era')
    def __str__(self):
        return f"{self.user_era_decade}"
