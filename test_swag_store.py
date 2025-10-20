import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.swag_login_page import SwagLoginPage
from pages.swag_inventory_page import SwagInventoryPage
from pages.swag_cart_page import SwagCartPage
from pages.swag_checkout_page import SwagCheckoutPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(service=service, options=options)
    yield drv
    drv.quit()


def test_swag_store_checkout(driver):
    login_page = SwagLoginPage(driver)
    inventory_page = SwagInventoryPage(driver)
    cart_page = SwagCartPage(driver)
    checkout_page = SwagCheckoutPage(driver)

    # 1. Открываем сайт
    login_page.open()

    # 2. Авторизация
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавляем товары
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")

    # 4. Переходим в корзину
    inventory_page.go_to_cart()

    # 5. Нажимаем Checkout
    cart_page.click_checkout()

    # 6. Заполняем форму
    checkout_page.fill_information("Arsen", "Testov", "12345")

    # 7. Проверяем итоговую сумму
    total = checkout_page.get_total_price()
    assert total == "58.29", f"Ожидалась сумма $58.29, но получили ${total}"
