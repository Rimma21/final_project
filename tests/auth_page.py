from pages.auth_page_wildb import AuthPageWildb


def test_check_auth_form_exist(web_browser):
    page = AuthPageWildb(web_browser)
    page.enter_button.click()
    assert page.auth_form_title.get_text() == 'Войти или создать профиль'


def test_enter_number(web_browser):
    page = AuthPageWildb(web_browser)
    page.enter_button.click()
    assert page.auth_form_title.get_text() == 'Войти или создать профиль'

    page.phone_number_input.send_keys('7078383299')
    # assert page.get_code_button.is() == True
    time.sleep(5)
