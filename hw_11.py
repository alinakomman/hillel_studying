import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebApp:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    def teardown_method(self):
        self.driver.quit()

    def test_signup(self):
        sign_up_button = self.driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()
        name_field = self.driver.find_element(By.ID, "signupName")
        name_field.send_keys("Lesya")
        lastname_field = self.driver.find_element(By.ID, "signupLastName")
        lastname_field.send_keys("Ukrainka")
        email_field = self.driver.find_element(By.ID, "signupEmail")
        email_field.send_keys("lesyaukrainka6666@gmail.com")
        password_field = self.driver.find_element(By.ID, "signupPassword")
        password_field.send_keys("xHvFsck7!Y9H7Fw")
        repeat_password_field = self.driver.find_element(By.ID, "signupRepeatPassword")
        repeat_password_field.send_keys("xHvFsck7!Y9H7Fw")
        confirmation_register_button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
        confirmation_register_button.click()

        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p"), "You don’t have any cars in your garage"))
        assert element is not None
