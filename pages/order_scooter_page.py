import allure
#from tests.conftest import driver
from locators import order_scooter_locators
from pages.base_page import BasePage


class OrderScooter(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step("Нажимаем кнопку Заказать")
    def click_order_button_upper(self):
        button = self.find_element(order_scooter_locators.ORDER_BUTTON_UPPER)
        button.click()

    @allure.step("Заполняем поле Имя")
    def set_name_field(self, name):
        name_input = self.find_element(order_scooter_locators.NAME_FIELD)
        name_input.send_keys(name)

    @allure.step("Заполняем поле Фамилия")
    def set_surname_field(self, surname):
        surname_input = self.find_element(order_scooter_locators.SURNAME_FIELD)
        surname_input.send_keys(surname)

    @allure.step("Заполняем поле Адрес")
    def set_address_field(self, address):
        address_input = self.find_element(order_scooter_locators.ADDRESS_FIELD)
        address_input.send_keys(address)

    @allure.step("Выбираем станцию метро")
    def set_metro_station(self, locator):
        station = self.find_element(order_scooter_locators.METRO_FIELD)
        station.click()
        selected_station = self.find_element(locator)
        selected_station.click()

    @allure.step("Заполняем поле Телефон")
    def set_phone_field(self, phone):
        phone_input = self.find_element(order_scooter_locators.PHONE_FIELD)
        phone_input.send_keys(phone)

    @allure.step("Нажимаем кнопку Далее")
    def click_next_button(self):
        next_button = self.find_element(order_scooter_locators.NEXT_BUTTON)
        next_button.click()

    @allure.step("Выбираем дату доставки")
    def set_delivery_date(self, locator):
        date_field = self.find_element(order_scooter_locators.DATE_FIELD)
        date_field.click()
        selected_date = self.find_element(locator)
        selected_date.click()

    @allure.step("Выбираем срок аренды")
    def set_rental_time(self, locator):
        rental_field = self.find_element(order_scooter_locators.RENTAL_TIME_FIELD)
        rental_field.click()
        selected_rental_field = self.find_element(locator)
        selected_rental_field.click()

    @allure.step("Выбираем цвет самоката")
    def set_color_scooter(self, locator):
        scooter_color = self.find_element(locator)
        scooter_color.click()

    @allure.step("Пишем комментарий для курьера")
    def set_comment(self, comment):
        comment_input = self.find_element(order_scooter_locators.COMMENT_FIELD)
        comment_input.send_keys(comment)

    @allure.step("Нажимаем заказать, после заполнения всех полей")
    def click_order_button_lower(self):
        button = self.find_element(order_scooter_locators.ORDER_BUTTON_LOWER)
        button.click()

    @allure.step("Подтверждаем заказ")
    def click_accept_button(self):
        accept_button = self.find_element(order_scooter_locators.ACCEPT_BUTTON)
        accept_button.click()

    @allure.step("Получаем текст кнопки Проверить статус")
    def get_text_status_button(self):
        status_button = self.find_element(order_scooter_locators.SEE_STATUS_BUTTON)
        return status_button.text
