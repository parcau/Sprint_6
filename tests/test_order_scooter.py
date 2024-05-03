from data import ClientData1
from data import ClientData2
from locators import order_scooter_locators
from pages.order_scooter_page import OrderScooter
import allure
import pytest
from conftest import driver


class TestOrderScooter:
    @allure.title("Проверяем заказ самоката по двум позитивным сценариям")
    @pytest.mark.parametrize(
        "name, surname, address, station, phone, date, rent, color, comment",
        [
            (
                ClientData1.NAME1,
                ClientData1.SURNAME1,
                ClientData1.ADDRESS1,
                order_scooter_locators.STATION_SOKOLNIKI,
                ClientData1.PHONE1,
                order_scooter_locators.DATA1_CHOOSE,
                order_scooter_locators.RENT_TWO_DAYS,
                order_scooter_locators.BLACK_COLOR_SCOOTER,
                ClientData1.COMMENT1,
            ),
            (
                ClientData2.NAME2,
                ClientData2.SURNAME2,
                ClientData2.ADDRESS2,
                order_scooter_locators.STATION_OHOTNYI_RYAD,
                ClientData2.PHONE2,
                order_scooter_locators.DATA2_CHOOSE,
                order_scooter_locators.RENT_FIVE_DAYS,
                order_scooter_locators.GREY_COLOR_SCOOTER,
                ClientData2.COMMENT2,
            ),
        ],
    )
    def test_order_scooter(
        self, driver, name, surname, address, station, phone, date, rent, color, comment
    ):
        order_scooter_page = OrderScooter(self)
        order_scooter_page.click_order_button_upper(driver)
        order_scooter_page.set_name_field(driver, name)
        order_scooter_page.set_surname_field(driver, surname)
        order_scooter_page.set_address_field(driver, address)
        order_scooter_page.set_metro_station(driver, station)
        order_scooter_page.set_phone_field(driver, phone)
        order_scooter_page.click_next_button(driver)
        order_scooter_page.set_delivery_date(driver, date)
        order_scooter_page.set_rental_time(driver, rent)
        order_scooter_page.set_color_scooter(driver, color)
        order_scooter_page.set_comment(driver, comment)
        order_scooter_page.click_order_button_lower(driver)
        order_scooter_page.click_accept_button(driver)
        assert order_scooter_page.get_text_status_button(driver) == "Посмотреть статус"
