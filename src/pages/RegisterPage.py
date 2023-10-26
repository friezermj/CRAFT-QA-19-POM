# from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, "//input[@name='username']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("f197")

    def set_email(self, email):
        self.driver.find_element(By.XPATH, "//input[@name='email']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("F1941@gmail.com")

    # def id_generator(self):
    # self.driver.find_element(By.CSS_SELECTOR, "p[class='text-white'] strong mark").rightclick().sen_key(key.ARROW_DOWN).send_key(key.ENTER)

    def click_on_register(self):
        self.driver.find_element(By.XPATH, "//input[@value='Register']").click()

