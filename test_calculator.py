import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")


    drv = webdriver.Chrome(service=service, options=options)
    yield drv
    drv.quit()


def test_slow_calculator_addition(driver):
    page = CalculatorPage(driver)

    page.open()
    page.set_delay(45)
    page.press("7")
    page.press("+")
    page.press("8")
    page.press("=")


    actual = page.wait_until_screen_shows("15", timeout=60)
    assert actual == "15"
