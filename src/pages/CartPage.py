from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_cart(self):
        self.driver.find_element(By.XPATH, "//a[@class='nav-link fa text-white']").click()

