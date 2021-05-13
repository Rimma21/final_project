#!/usr/bin/python3
# -*- encoding=utf8 -*-
from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class MainPageWildberries(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://wildberries.ru'

            super().__init__(web_driver, url)

    search = WebElement(xpath='//body/div[1]/header[1]/div[1]/div[2]/div[3]/div[1]/input[1]')

    search_button = WebElement(xpath='//body/div[1]/header[1]/div[1]/div[2]/div[3]/div[1]/div[2]/button[2]')

    search_title = WebElement(xpath='//*[@id="catalog"]/div[1]/div[1]/h1[1]')

    product_titles = ManyWebElements(xpath='//*[@id="catalog-content"]/div[4]/div[7]/div[1]/span[1]/span[1]/span['
                                           '1]/a[1]/div[2]/div[3]')

    # todo: неправильно прописан  xpath
    product = WebElement(xpath='//*[@id="c7004000"]/img[1]')

    product_price = ManyWebElements(
        xpath='//*[@id="catalog-content"]/div[4]/div[1]/div[1]/span[1]/span[1]/span[1]/a[1]/div[2]/div[2]/span['
              '1]/ins[1]')

    product_rating = ManyWebElements(
        xpath='//*[@id="catalog-content"]/div[4]/div[1]/div[1]/span[1]/span[1]/span[1]/a[1]/span[1]/span[1]/span[2]')

    product_discounts = ManyWebElements(
        xpath='//*[@id="catalog-content"]/div[4]/div[1]/div[1]/span[1]/span[1]/span[1]/a[1]/div[2]/div[2]/span[1]/span[1]/span[1]')

    product_price_discount = ManyWebElements(
        xpath='//*[@id="catalog-content"]/div[4]/div[1]/div[1]/span[1]/span[1]/span[1]/a[1]/div[2]/div[2]/span[1]/span[1]/del[1]')

    discount_button_10 = WebElement(xpath='//*[@id="filterPanelLeft"]/div[2]/div[2]/div[1]/div[1]/fieldset[1]/label[1]')

    discount_button_30 = WebElement(xpath='//*[@id="filterPanelLeft"]/div[2]/div[2]/div[1]/div[1]/fieldset[1]/label[2]')

    discount_button_50 = WebElement(xpath='//*[@id="filterPanelLeft"]/div[2]/div[2]/div[1]/div[1]/fieldset[1]/label[3]')

    breadcrumbs = ManyWebElements(xpath='//*[@id="catalog-content"]/div[2]/ul[1]/li[1]')

    product_card_title = WebElement(xpath='//*[@id="container"]/div[1]/div[2]/div[1]/div[1]')

    product_card_price = WebElement(
        xpath='//*[@id="container"]/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/span[1]')

    product_card_articul = WebElement(xpath='//*[@id="container"]/div[1]/div[2]/div[2]/div[1]/span[1]')

    product_card_description = WebElement(xpath='//*[@id="container"]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/h1[1]')

    product_card_composition = WebElement(xpath='//*[@id="container"]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/h1[1]')

    product_card_seller = WebElement(xpath='//*[@id="Comments"]/div[1]/div[1]/div[3]/div[2]')

    product_card_fast_view_detail_but = WebElement(xpath='//*[@id="container"]/div[3]/a[1]')

    product_card_size_title = WebElement(xpath='//*[@id="container"]/div[1]/div[2]/div[4]/div[7]/div[1]/p[1]')
    product_card_size = ManyWebElements(xpath='//*[@id="container"]/div[1]/div[2]/div[4]/div[7]/div[2]/label[1]')
    product_description_maximize = WebElement(xpath='//*[@id="container"]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]')

    product_description_minimize = WebElement(xpath='//*[@id="container"]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]')

    product_comment_rules_but = WebElement(xpath='//*[@id="container"]/div[3]/a[1]')
    product_comment_rules_desc = WebElement(xpath='body/div[1]/p[1]/h4[1]')