from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


    _delay_input = (By.CSS_SELECTOR, "#delay")
    _screen_candidates = [
        (By.CSS_SELECTOR, ".screen"),
        (By.CSS_SELECTOR, "#screen"),
    ]

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)


    def open(self):
        self.driver.get(self.URL)


    def set_delay(self, seconds: int):
        """Вводим задержку в поле #delay."""
        delay = self.wait.until(EC.element_to_be_clickable(self._delay_input))
        delay.clear()
        delay.send_keys(str(seconds))

    def press(self, label: str):
        xpath = f"//button[normalize-space()='{label}'] | //span[normalize-space()='{label}']"
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn.click()


    def _screen_element(self):
        last_err = None
        for locator in self._screen_candidates:
            try:
                return self.wait.until(EC.presence_of_element_located(locator))
            except Exception as e:
                last_err = e
        raise last_err

    def get_screen_text(self) -> str:
        return self._screen_element().text.strip()

    def wait_until_screen_shows(self, expected: str, timeout: int = 60) -> str:
        screen = self._screen_element()
        WebDriverWait(self.driver, timeout).until(
            lambda d: screen.text.strip() == expected
        )
        return screen.text.strip()
