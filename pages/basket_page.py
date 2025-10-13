from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage): 
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.HAS_BASKET_ITEMS),"Basket should be empty, but basket has items"

    def should_be_basket_is_empty_notification(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_NOTIFICATION),"Should be basket is empty notification, but there's no such notification"
        