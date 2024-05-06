import allure
#from conftest import driver
from locators import main_page_locators
from pages.base_page import BasePage


class QuestionsAboutTheImportant(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step("Скролл страницы")
    def scroll(self):
        element = self.find_element(main_page_locators.SEVENTH_QUESTION)
        self.execute_script(element)

    @allure.step("Кликаем по вопросу")
    def click_on_question(self, locator):
        button = self.find_element(locator)
        button.click()

    @allure.step("Выводим текст ответа")
    def answer_text(self, locator):
        answer_text = self.find_element(locator)
        return answer_text.text


class NavigationOnSite(BasePage):
    @allure.step("Кликаем по лого Самоката")
    def click_logo_scooter(self):
        logo_scooter = self.find_element(main_page_locators.SCOOTER_LOGO)
        logo_scooter.click()

    @allure.step("Кликаем по кнопка Заказать")
    def click_order_button(self):
        order_button = self.find_element(main_page_locators.ORDER_BUTTON)
        order_button.click()

    @allure.step("Узнаем URL текущей страницы")
    def get_current_url(self):
        return self.current_url()

    @allure.step("Кликаем по лого Яндекса")
    def click_yandex_logo(self):
        yandex_logo = self.find_element(main_page_locators.YANDEX_LOGO)
        yandex_logo.click()

    @allure.step("Переключаемся на другую вкладку")
    def switch_on_tab(self):
        self.switch_to_window()

    @allure.step('Ожидаем наличие кнопки Найти')
    def wait_visibility_search_button(self):
        self.wait_visibility_element(main_page_locators.DZEN_SEARCH_BUTTON)
        return self.find_element(main_page_locators.DZEN_SEARCH_BUTTON)
