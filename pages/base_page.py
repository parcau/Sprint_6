import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидаем наличия кликабельного элемента на странице")
    def wait_clickable_element(self, driver, locator):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return driver.find_element(*locator)
