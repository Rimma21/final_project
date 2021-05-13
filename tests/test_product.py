#!/usr/bin/python3
# -*- encoding=utf8 -*-
import time

from pages.product import MainPageWildberries


def test_check_search(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    for title in page.product_titles.get_text():
        assert 'adidas' in title.lower()


def test_check_search_product_cnt(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert page.product_titles.count() == 100


def test_check_product_card(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.product.click()


def test_check_product_price(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    for price in page.product_price.get_text():
        assert price != ""


# # проверка рейтинга товара положительный
def test_check_rating(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    for rating in page.product_rating.get_text():
        assert rating != ""


# # проверка рейтинга товара негативный
def test_check_rating_fail(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    for rating in page.product_rating.get_text():
        assert rating == ""


# проверка скидочной цены, если есть скидка
def test_discount_price_exist(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    product_discount = page.product_discount.get_text()
    if product_discount != "":
        product_price_discount = page.product_price_discount.get_text()
        assert product_price_discount != ""

def test_discount_price_exist(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    product_discount = page.product_discount.get_text()
    if product_discount != "":
        product_price_discount = page.product_price_discount.get_text()
        assert product_price_discount == ""

# z проверка товаров со скидкой больше 10%
def test_10_discount_percent_click(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_10.click()

    for product_discount in page.product_discounts.get_text():
        if product_discount != "":
            # -43
            replaced_disc = product_discount.replace("-", "")
            replaced_disc = replaced_disc.replace("%", "")
            assert int(replaced_disc) >= 8


def test_10_discount_percent_click_err(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_10.click()

    for product_discount in page.product_discounts.get_text():
        if product_discount != "":
            # -43
            replaced_disc = product_discount.replace("-", "")
            replaced_disc = replaced_disc.replace("%", "")
            assert int(replaced_disc) < 8


# # z проверка товаров со скидкой больше 30%
def test_30_discount_percent_click(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_30.click()

    for product_discount in page.product_discounts.get_text():
        if product_discount != "":
            # -43
            replaced_disc = product_discount.replace("-", "")
            replaced_disc = replaced_disc.replace("%", "")
            assert int(replaced_disc) >= 28


def test_30_discount_percent_click_err(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_30.click()

    for product_discount in page.product_discounts.get_text():
        if product_discount != "":
            # -43
            replaced_disc = product_discount.replace("-", "")
            replaced_disc = replaced_disc.replace("%", "")
            assert int(replaced_disc) < 28


# z проверка товаров со скидкой больше 50%
def test_50_discount_percent_click(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_50.click()

    time.sleep(2)

    for product_discount in page.product_discounts.get_text():
        if product_discount != "":
            # -43
            replaced_disc = product_discount.replace("-", "")
            replaced_disc = replaced_disc.replace("%", "")
            assert int(replaced_disc) >= 49


# z проверка товаров со скидкой больше 50%
def test_50_discount_percent_click_err(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_50.click()

    time.sleep(2)

    for product_discount in page.product_discounts.get_text():
        if product_discount != "":
            # -43
            replaced_disc = product_discount.replace("-", "")
            replaced_disc = replaced_disc.replace("%", "")
            assert int(replaced_disc) < 49


# проверка появление выбранного фильтра над карточками
def test_50_discount_breadcrumb_onclick(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_50.click()
    time.sleep(2)

    for breadcrumb in page.breadcrumbs.get_text():
        assert breadcrumb == 'от 50% и выше'


def test_50_discount_breadcrumb_onclick_err(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.discount_button_50.click()
    time.sleep(2)

    for breadcrumb in page.breadcrumbs.get_text():
        assert breadcrumb != 'от 50% и выше'


def test_10_discount_breadcrumb_onclick(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_10.click()
    time.sleep(2)

    for breadcrumb in page.breadcrumbs.get_text():
        assert breadcrumb == 'от 10% и выше'


def test_30_discount_breadcrumb_onclick(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_30.click()
    time.sleep(2)

    for breadcrumb in page.breadcrumbs.get_text():
        assert breadcrumb == 'от 30% и выше'


def test_10_discount_breadcrumb_onclick_err(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_10.click()
    time.sleep(2)

    for breadcrumb in page.breadcrumbs.get_text():
        assert breadcrumb != 'от 10% и выше'


def test_30_discount_breadcrumb_onclick_err(web_browser):
    page = MainPageWildberries(web_browser)
    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()

    page.discount_button_30.click()
    time.sleep(2)

    for breadcrumb in page.breadcrumbs.get_text():
        assert breadcrumb != 'от 30% и выше'
