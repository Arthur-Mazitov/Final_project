from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage): 
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        time.sleep(1)
        self.solve_quiz_and_get_code()         
    
    def is_book_name_correct(self):
        BOOK_NAME_IN_ALERT = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT)
        BOOK_NAME = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert BOOK_NAME_IN_ALERT.text == BOOK_NAME.text
    
    def is_price_correct(self):
        PRICE_IN_ALERT = self.browser.find_element(*ProductPageLocators.PRICE_IN_ALERT)
        PRICE = self.browser.find_element(*ProductPageLocators.PRICE)
        assert PRICE_IN_ALERT.text == PRICE.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is not presented, but should be"
    
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message has not dissapeared"
    
    


    