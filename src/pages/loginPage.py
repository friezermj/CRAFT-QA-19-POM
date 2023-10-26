from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, "// input[ @ value = 'Login']").click()

    def enter_user_id(self):
        self.driver.find_element(By.XPATH, "//input[@name='userid']").send_keys(2918)

    def click_on_login_button_again(self):
        self.driver.find_element(By.XPATH, "// input[ @ value = 'Login']").click()




