import pytest
import requests
from selenium import webdriver

from facade.registration_facade import RegistrationFacade


class TestBase:
    def setup_method(self):  # тут кожного разу створюʼмо новий вебдрайвер та нову сесію для кожного окремого тесту
        self._driver = webdriver.Chrome()  # протекшен мемборів з _ які можуть використовуватися тільки в наслідстві
        self._session = requests.session()
        self._registration_facade = RegistrationFacade(self._driver)



        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")


class TestRegistration(TestBase):

    def setup_class(self):
        # self.session = requests.session()
        self.user_email = "symonenkovasyl@gmail.com"
        self.user_password = "xHvFsck7!Y9H7Fw"

        self.user_to_login = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }
#   def setup_class(self):                                                                  
#       with open('users.json', 'r') as f:                                                  
#           users_data = json.load(f)                                                       
#                                                                                           
#       self.users_to_register = [(user['email'], user['password']) for user in users_data] 

    def teardown_method(self):
        self._session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user_to_login)
        self._session.delete(url="https://qauto2.forstudy.space/api/users")
        self._driver.quit()

    def test_signup(self):
        self._registration_facade.register_user("Vasyl", "Symonenko", self.user_email, self.user_password, self.user_password)
        assert self._registration_facade.check_is_user_logged_in()

#   @pytest.mark.parametrize("email, password", self.users_to_register)                             
#   def test_signup(self, email, password):                                                         
#       self._registration_facade.register_user("Vasyl", "Symonenko", email, password, password)    
#       assert self._registration_facade.check_is_user_logged_in()                                  

  
