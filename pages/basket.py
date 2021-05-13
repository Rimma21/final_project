#!/usr/bin/python3
# -*- encoding=utf8 -*-
from pages.base import WebPage
from pages.elements import WebElement


class Basket(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://wildberries.ru'

            super().__init__(web_driver, url)

    basket = WebElement(xpath='//*[@id="basketContent"]/div[3]/a[1]')
    empty_basket = WebElement(xpath='//*[@id="app"]/div[1]/div[1]/div[1]/div[1]/h3[1]')





