from selenium.webdriver.common.by import By


class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    def click_register(self):
        self.driver.find_element(By.XPATH, "//input[@value='Register']").click()
