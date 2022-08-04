from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import *
from flask_testing import TestCase

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
        user1 = user(forename = 'Sample', surname = 'User')
        barbie_era1 = barbie_era(user=1,barbie_year='1950',birth_year='1950')
        db.session.add(user1)
        db.session.add(barbie_era1)
        db.session.commit()

    def  tearDown(self): # runs after every test 
        db.session.remove() #remove any active database sessions
        db.drop_all()
    
class TestView(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)
        self.assertIn(b'Barbie Era', response.data)

    def test_view_user(self):
        response = self.client.get(url_for('all_users'))
        self.assert200(response)
        self.assertIn(b'Users', response.data)

    def test_view_era(self):
        response = self.client.get(url_for('view_barbie_era'))
        self.assert200(response)
        self.assertIn(b'barbie', response.data)

    def test_add_user(self):
        response = self.client.get(url_for('add_new_user'))
        self.assert200(response)
        self.assertIn(b'forename', response.data)

    def test_get_user_era(self):
        response = self.client.get(url_for('get_user_era',year=1950))
        self.assert200(response)
        self.assertIn(b'barbie era', response.data)

    def test_add_era(self):
        response = self.client.get(url_for('add_barbie_era'))
        self.assert200(response)

    def test_update_users(self):
        response = self.client.get(url_for('update_users', id=1))
        self.assert200(response)

    def test_update_user_era(self):
        response = self.client.get(url_for('update_barbie_era',id=1))
        self.assert200(response)

    def test_delete_user(self):
        response = self.client.get(url_for('delete_users',id=1), follow_redirects = True )
        self.assert200(response)
    
    def test_user_era(self):
        response = self.client.get(url_for('delete_barbie_era',id=1), follow_redirects = True )
        self.assert200(response)

# creating a new test class for the post requests 

class TestPostRequests(TestBase):
    def test_post_add_user(self):
        response = self.client.post(
            url_for('add_new_user'),
            data = dict(forename= 'Sample', surname= 'User'),
            follow_redirects = True)
        self.assert200 (response)
        assert user.query.filter_by(forename='Sample').first() is not None

    def test_post_update_user(self):
        response = self.client.post(
            url_for('update_users', id=1),
            data = dict(forename= 'New', surname= 'User'),
            follow_redirects=True
        )
        self.assert200(response)
        self.assertIn(b'Barbie', response.data)
      

    def test_post_add_era(self):
        response = self.client.post(
            url_for('add_barbie_era'),
            data = dict(barbie_year ='1950', birth_year='1950', user=1),
            follow_redirects = True)
        self.assert200 (response)
        assert barbie_era.query.filter_by(barbie_year='1950').first() is not None
        

    def test_post_update_era(self):
        response = self.client.post(
            url_for('update_barbie_era', id=1),
            data = dict(barbie_year ='2000', birth_year='2000', user_era =1),
            follow_redirects = True)
        self.assert200 (response)
        self.assertIn(b'Barbie', response.data)
    