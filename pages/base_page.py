from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def execute_script(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def current_url(self):
        return self.driver.current_url
