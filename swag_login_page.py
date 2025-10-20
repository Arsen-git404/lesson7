from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SwagLoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        user_input = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        pwd_input = self.driver.find_element(By.ID, "password")
        login_btn = self.driver.find_element(By.ID, "login-button")

        user_input.clear()
        user_input.send_keys(username)
        pwd_input.clear()
        pwd_input.send_keys(password)
        login_btn.click()
