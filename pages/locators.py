from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form']")
    REGISTER_FORM = (By.CSS_SELECTOR, "form[id='register_form']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "form[id='add_to_basket_form']>button")
    BOOK_NAME = (By.CSS_SELECTOR, "div>h1")
    BOOK_NAME_IN_ALERT = (By.CSS_SELECTOR, "div[class='alertinner ']>strong")
    PRICE = (By.CSS_SELECTOR, "div>p[class='price_color']")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, "div[class='alertinner ']>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div:nth-child(2)>div[class='alertinner ']>strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
