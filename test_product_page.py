from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.should_be_basket_is_empty_notification()
    page.basket_should_be_empty()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, self.link)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "12345678"
        page.open()
        page.register_new_user(email=email, password=password)
        page = BasePage(browser, self.link)
        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.is_book_name_correct()
        page.is_price_correct()
        page.should_be_success_message()
    