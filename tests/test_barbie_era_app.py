from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import *
from flask_testing import TestCase
from datetime import date

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-app.db', # new database to not break the production database
            WTF_CRSF_ENABLED=False, 
            DEBUG = True
            )

        return app
        
    def setUp(self): # runs before each test that we run 
        db.create_all()
        user1 = user(forename = 'Abbey', surname = 'Detrick', dob = date(2022,6,7))
        era1= barbie_era(era_decade = 1950)
        userera1 = user_era(user_era_decade = 1950)
        db.session.add(user1)
        db.session.add(era1)
        db.session.add(userera1)
        db.session.commit()

    def  tearDown(self): # runs after every test 
        db.session.remove() #remove any active database sessions
        db.drop_all()
    
class TestHome(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)
        self.assertIn(b'Barbie Era', response.data)
    def test_view_user(self):
        response = self.client.get(url_for('all_users'))
        self.assert200(response)
    def test_view_era(self):
        response = self.client.get(url_for('view_all_era'))
        self.assert200(response)
    def test_user_era(self):
        response = self.client.get(url_for('view_user_era'))
        self.assert200(response)

    # def test_add_user(self):# testing the create functionality of crud
    #     response = self.client.get(url_for('add_new_user'))
    #     self.assert200(response)
    #     self.assertIn(b' forename', response.data)
    # def test_add_era(self):
    #     response = self.client.get(url_for('new_barbie_era'))
    #     self.assert200(response)
    #     self.assertIn(b' era_decade', response.data)
