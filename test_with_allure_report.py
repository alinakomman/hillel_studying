import allure
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from facade.registration_facade import RegistrationFacade


class TestBase:
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.session()
        self._registration_facade = RegistrationFacade(self._driver)

        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")


class TestRegistration(TestBase):
    def setup_class(self):
        self.user_email = "lesya.ukrainka@test.com"
        self.user_password = "uHjusss&2RRv"

        self.user_to_login = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def teardown_method(self):
        self._session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user_to_login)
        self._session.delete(url="https://qauto2.forstudy.space/api/users")
        self._driver.quit()

    @allure.feature("Registration Tests")
    @allure.story("Test registration using facade")
    @allure.issue("https://google.com", name="(CLOSED) Link for very important bug")
    @allure.link("https://google.com", name="Link to TestRail")
    def test_registration_test(self):
        with allure.step("Register user using facade"):
            self._registration_facade.register_user("Lesia", "Ukrainka", self.user_email, self.user_password,
                                                    self.user_password)
        with allure.step("Check if user is logged in"):
            assert self._registration_facade.check_is_user_logged_in()

    @allure.feature("Registration Tests")
    @allure.story("Test registration without facade")
    def test_registration_1_test(self):
        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

        with allure.step("Click Sign up button"):
            sign_up_button = self._driver.find_element(By.XPATH, "//button[text()='Sign up']")
            sign_up_button.click()

        with allure.step("Fill registration form"):
            name_field = self._driver.find_element(By.ID, "signupName")
            name_field.send_keys("Vasyl")
            last_name_field = self._driver.find_element(By.ID, "signupLastName")
            last_name_field.send_keys("Stus")
            email_field = self._driver.find_element(By.ID, "signupEmail")
            email_field.send_keys(self.user_email)
            password_field = self._driver.find_element(By.ID, "signupPassword")
            password_field.send_keys(self.user_password)
            repeat_password_field = self._driver.find_element(By.ID, "signupRepeatPassword")
            repeat_password_field.send_keys(self.user_password)

        with allure.step("Confirm of Registration"):
            register_button = self._driver.find_element(By.XPATH, '//button[text()="Register"]')
            register_button.click()

        with allure.step("Verify registration success"):
            empty_garage = self._driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")
            assert len(empty_garage) != 0
