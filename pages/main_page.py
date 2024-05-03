import allure
from conftest import driver
from locators import main_page_locators
from pages.base_page import BasePage


class QuestionsAboutTheImportant(BasePage):
    @allure.step("Скролл страницы")
    def scroll(self, driver):
        element = driver.find_element(*main_page_locators.SEVENTH_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликаем по вопросу")
    def click_on_question(self, driver, locator):
        button = driver.find_element(*locator)
        button.click()

    @allure.step("Выводим текст ответа")
    def answer_text(self, driver, locator):
        answer_text = driver.find_element(*locator)
        return answer_text.text


class NavigationOnSite(BasePage):
    @allure.step("Кликаем по лого Самоката")
    def click_logo_scooter(self, driver):
        logo_scooter = driver.find_element(*main_page_locators.SCOOTER_LOGO)
        logo_scooter.click()

    @allure.step("Кликаем по кнопка Заказать")
    def click_order_button(self, driver):
        order_button = driver.find_element(*main_page_locators.ORDER_BUTTON)
        order_button.click()

    @allure.step("Узнаем URL текущей страницы")
    def get_current_url(self, driver):
        return driver.current_url

    @allure.step("Кликаем по лого Яндекса")
    def click_yandex_logo(self, driver):
        yandex_logo = driver.find_element(*main_page_locators.YANDEX_LOGO)
        yandex_logo.click()

    @allure.step("Переключаемся на другую вкладку")
    def switch_on_tab(self, driver):
        return driver.switch_to.window(driver.window_handles[1])
