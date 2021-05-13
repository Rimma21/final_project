Introduction
------------

В репозитории код для тестирования http://wildberries.ru 


Files
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pages/base.py](pages/base.py) contains PageObject pattern implementation for Python.

[pages/elements.py](pages/elements.py) contains helper class to define web elements on web pages.

[tests/test_auth_page.py](tests/test_auth_page.py) тест авторизации в wildberries.ru
[tests/test_basket.py](tests/test_basket.py) тест корзины
[tests/test_product.py](tests/test_product.py) тест поиска товаров
[tests/test_product_card.py](tests/test_product_card.py) тест карточки товара


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```

   ![alt text](example.png)

Note:
~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.