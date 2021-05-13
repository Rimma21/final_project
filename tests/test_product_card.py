#!/usr/bin/python3
# -*- encoding=utf8 -*-
import time

from pages.product import MainPageWildberries


def test_description_max_click(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()

    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    page.product_description_maximize.click()
    assert page.product_description_minimize.get_text() == 'Свернуть описание'


def test_description_max_click_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()

    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    page.product_description_maximize.click()
    assert page.product_description_minimize.get_text() != 'Свернуть описание'


def test_description_min_click(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    page.product_description_minimize.click()
    assert page.product_description_maximize.get_text() == 'Развернуть описание'


def test_description_min_click_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    page.product_description_minimize.click()
    assert page.product_description_maximize.get_text() != 'Развернуть описание'


def test_product_card_click(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_title.get_text() == ""


def test_product_card_click_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_title.get_text() != ""


def test_product_card_price(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_price.get_text() != ""


def test_product_card_price_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_price.get_text() == ""


def test_product_card_articul(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_articul.get_text() != ""


def test_product_card_articul_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_articul.get_text() == ""


def test_product_card_description(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_description.get_text() != ""


def test_product_card_description_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_description.get_text() == ""


def test_product_card_size_list_exist(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()
    assert page.product_card_size_title.get_text() != ""
    assert page.product_card_size.count() > 0


def test_product_card_size_list_exist_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()
    assert page.product_card_size_title.get_text() != ""
    assert page.product_card_size.count() == 0


def test_product_card_composition(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_composition.get_text() != ""


def test_product_card_composition_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_composition.get_text() == ""


def test_product_card_seller(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()

    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_seller.get_text() != ""


def test_product_card_seller_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()

    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_card_seller.get_text() == ""


def test_product_card_comment_link(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_comment_rules_but.get_text() != ""


def test_product_card_comment_link_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()
    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_comment_rules_but.get_text() == ""


def test_product_card_comment_desc_exist(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()

    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_comment_rules_but.get_text() == "Правила оформления отзывов и вопросов"

    page.product_comment_rules_but.click()
    assert page.product_comment_rules_desc.get_text() == "Правила оформления отзывов и вопросов"


def test_product_card_comment_desc_exist_err(web_browser):
    page = MainPageWildberries(web_browser)

    page.search = 'кроссовки adidas'
    page.search_button.click()
    assert 'кроссовки adidas' in page.search_title.get_text().lower()
    page.product.click()

    assert page.product_card_fast_view_detail_but.get_text().lower() == "больше информации о товаре"
    page.product_card_fast_view_detail_but.click()

    assert page.product_comment_rules_but.get_text() == "Правила оформления отзывов и вопросов"

    page.product_comment_rules_but.click()
    assert page.product_comment_rules_desc.get_text() != "Правила оформления отзывов и вопросов"
