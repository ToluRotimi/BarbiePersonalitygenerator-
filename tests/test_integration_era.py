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
            LIVESERVER_PORT = self.TEST_PORT,
            DEBUG = True,
            TESTING = True
        )

        return app
    def setUp(self):
        db.create_all()
        sample_user = user(forename="Alice", surname="Rodeo")
        db.session.add(sample_user)
        db.session.commit()
        options = webdriver.chrome.options.Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(f'http://localhost:{self.TEST_PORT}/create_barbie_era')

    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
    
class Testcreateera(TestBase):
    def submit_input(self, test_case):
        user_field = self.driver.find_element_by_xpath('/html/body/div/form/select[1]')
        barbie_year_field = self.driver.find_element_by_xpath('/html/body/div/form/select[2]')
        birth_year_field = self.driver.find_element_by_xpath('/html/body/div/form/select[3]]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
        user_field.send_keys(test_case[0])
        barbie_year_field.send_keys(test_case[1])
        birth_year_field.send_keys(test_case[2])
        submit.click()