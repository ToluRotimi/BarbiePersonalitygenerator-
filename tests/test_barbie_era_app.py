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
        user1 = user(forename = 'Abbey', surname = 'Detrick')
        userera1 = user_era(user_era_decade = 1950)
        db.session.add(user1)
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

    def test_user_era(self):
        response = self.client.get(url_for('view_user_era'))
        self.assert200(response)

    def test_add_user(self):
        response = self.client.get(url_for('add_new_user'))
        self.assert200(response)
        self.assertIn(b'forename', response.data)

    def test_get_user_era(self):
        response = self.client.get(url_for('get_user_era',year=1950))
        self.assert200(response)
        self.assertIn(b'barbie era', response.data)

    def test_add_user_era(self):
        response = self.client.get(url_for('add_user_era'))
        self.assert200(response)

    def test_update_users(self):
        response = self.client.get(url_for('update_users', id=1))
        self.assert200(response)

    def test_update_user_era(self):
        response = self.client.get(url_for('update_user_era'))
        self.assert200(response)

    def test_delete_user(self):
        response = self.client.get(url_for('delete_users',id=1), follow_redirects = True )
        self.assert200(response)
    
    def test_user_era(self):
        response = self.client.get(url_for('delete_user_era',id=1), follow_redirects = True )
        self.assert200(response)

# creating a new test class for the post requests 
class TestPostRequests(TestBase):
    def test_post_add_user(self):
        response = self.client.post(
            url_for('add_new_user'),
            data = dict(forename = 'Ted', surname = 'Maint'),
            follow_redirects = True)
        assert user.query.filter_by(forename='Ted').first() is not None
        self.assert200 (response)

    def test_post_update_user(self):
        response = self.client.post(
            url_for('update_user', id=1),
            data = dict(forename = 'alice', surname = 'Maint'),
            follow_redirects = True)
        assert user.query.filter_by(forename='alice').first() is not None
        assert user.query.filter_by(forename='Ted').first() is None
        self.assert200 (response)
        
    def test_post_add_user_era(self):
        response = self.client.post(
            url_for('add_user_era'),
            data = dict(user_era_decade = '1950', user_era =1),
            follow_redirects = True)
        assert user_era.query.filter_by(user_era_decade= '1950').first() is not None
        self.assert200 (response)
