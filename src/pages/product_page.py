from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def product_search(self):
        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("acer pc")

    def get_product_quick_view(self):
        self.driver.find_element(By.XPATH, "(//button[@type='button'])[6]").click()

    def product_quantity_selection(self):
        qty = self.driver.find_element(By.XPATH, "(//select[@class='form-control'])[8]")
        q = Select(qty)
        q.select_by_index(2)

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, "(//button[@type='submit'])[14]").click()






