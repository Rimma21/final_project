from pages.basket import Basket


def test_check_auth_form_exist(web_browser):
    page = Basket(web_browser)
    page.basket.click()
    assert page.empty_basket.get_text() == 'В вашей корзине пока ничего нет'

# def test_basket_is_not_empty(web_browser):