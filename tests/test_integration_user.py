from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import *
from application.forms import *

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-app.db',
            LIVESERVER_PORT= self.TEST_PORT,
            DEBUG=True,
            TESTING=True
        )

        return app
    
    def setUp(self):
        db.create_all()
        options=webdriver.chrome.options.Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(f'http://localhost:{self.TEST_PORT}/add_user') # this ensures that the add user is loaded in time with the test run

    def tearDown(self):
        self.driver.quit() #new driver instance for each test
        db.session.remove()
        db.drop_all()
    
class TestAdduser(TestBase):
    def submit_input(self, test_case):  #first need to identify elements that we want to interact with 
        forename_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')  #identifies the forename field on our form
        surname_field = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[4]')
        forename_field.send_keys(test_case[0])  # send keys takes a string and simulates a user typing the characters into the field being called 
        surname_field.send_keys(test_case[1])
        submit.click()

    def test_add_user(self):
        test_case = "Subo", "Rotimi"
        self.submit_input(test_case)
        assert list(user.query.all()) != []
        assert user.query.filter_by(forename="Subo").first() is not None

# ensuring that no entry was passed into calidator because it did not meet validation check
    def test_add_user_validation(self):
        test_case = "Tolu", ""
        self.submit_input(test_case)
        assert list(user.query.all()) == []
        assert user.query.filter_by(forename="Tolu").first() is None