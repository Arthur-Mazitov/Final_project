from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage): 
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        time.sleep(1)
        self.solve_quiz_and_get_code()

    