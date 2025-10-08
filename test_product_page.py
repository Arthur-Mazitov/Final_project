from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_book_name_correct()
    page.is_price_correct()
    page.should_not_be_success_message()