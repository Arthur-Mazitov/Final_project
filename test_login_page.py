from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/accounts/login/"

def test_guest_should_see_url_and_form(browser):
    
    # Выполняем проверки на окне логина
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()
