from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def input_text(self, locator, text: str):
        self.driver.find_element(*locator).send_keys(text)

    def assert_text(self, expected_text: str, locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def assert_partial_text(self, expected_text: str, locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"Expected {expected_text}, but got {actual_text}"





