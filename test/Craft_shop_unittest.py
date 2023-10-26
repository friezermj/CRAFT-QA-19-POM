from selenium import webdriver
import unittest
import time
from src.pages.RegisterPage import RegisterPage
from src.pages.loginPage import LoginPage
from src.pages.product_page import ProductPage
from src.pages.CartPage import CartPage
from src.pages.Landing_page import LandingPage
from src.pages.OrderPage import OrderPage


class CraftShopTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_valid(self):
        self.driver.get("http://shop.icraftsoft.net:8095/")
        time.sleep(3)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        signin = LandingPage(self.driver)
        signin.click_register()
        time.sleep(4)

        sign_in = RegisterPage(self.driver)
        sign_in.enter_username(self)
        time.sleep(2)
        sign_in.set_email(self)
        sign_in.click_on_register()
        time.sleep(2)

        log_in = LoginPage(self.driver)
        log_in.click_on_login_button()
        log_in.enter_user_id()
        time.sleep(2)
        log_in.click_on_login_button_again()
        time.sleep(2)

        product = ProductPage(self.driver)
        product.product_search()
        time.sleep(2)
        product.get_product_quick_view()
        time.sleep(2)
        product.product_quantity_selection()
        time.sleep(2)
        product.add_to_cart()

        cart = CartPage(self.driver)
        cart.click_on_cart()
        time.sleep(2)

        order = OrderPage(self.driver)
        order.click_on_buy_now()
        time.sleep(2)
        order.get_home()
        print("Test completed")


if __name__ == '__main__':
    unittest.main()
