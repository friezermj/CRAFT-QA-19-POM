from selenium.webdriver.common.by import By


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_buy_now(self):
        self.driver.find_element(By.XPATH, "//input[@value='Buy Now']").click()

    def get_home(self):
        self.driver.find_element(By.XPATH, "(//input[contains(@value,'Home')])[2]").click()




