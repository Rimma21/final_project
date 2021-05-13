import os

from pages.base import WebPage
from pages.elements import WebElement


class AuthPageWildb(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://wildberries.ru'

        super().__init__(web_driver, url)

    enter_button = WebElement(xpath='//*[@id="basketContent"]/div[2]/a[1]')
    auth_form_title = WebElement(xpath='//*[@id="spaAuthForm"]/div[1]/div[1]/h2[1]')

    phone_number_input = WebElement(xpath='//*[@id="spaAuthForm"]/div[1]/div[2]/div[1]/div[2]/div[2]/input[1]')

    get_code_button = WebElement(xpath='//*[@id="requestCode"]')
