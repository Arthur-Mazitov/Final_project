from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_go_to_login_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    