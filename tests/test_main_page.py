import pytest
from data import Urls
from locators import main_page_locators
from conftest import driver
from pages.main_page import QuestionsAboutTheImportant
from pages.main_page import NavigationOnSite
from data import MainPageAnswerToQuestion
import allure


class TestDropDownList:
    @allure.title("Кликаем по вопросам и проверяем, что появляются ответы")
    @pytest.mark.parametrize(
        "question, answer, true_answer",
        [
            (
                main_page_locators.FIRST_QUESTION,
                main_page_locators.FIRST_QUESTION_ACTIVE,
                MainPageAnswerToQuestion.FISRT_QUESTION_ANSWER,
            ),
            (
                main_page_locators.SECOND_QUESTION,
                main_page_locators.SECOND_QUESTION_ACTIVE,
                MainPageAnswerToQuestion.SECOND_QUESTION_ANSWER,
            ),
            (
                main_page_locators.THIRD_QUESTION,
                main_page_locators.THIRD_QUESTION_ACTIVE,
                MainPageAnswerToQuestion.THIRD_QUESTION_ANSWER,
            ),
            (
                main_page_locators.FOURTH_QUESTION,
                main_page_locators.FOURTH_QUESTION_ACTIVE,
                MainPageAnswerToQuestion.FOURTH_QUESTION_ANSWER,
            ),
            (
                main_page_locators.FIFTH_QUESTION,
                main_page_locators.FIFTH_QUESTION_ACTIVE,
                MainPageAnswerToQuestion.FIFTH_QUESTION_ANSWER,
            ),
            (
                main_page_locators.SIXTH_QUESTION,
                main_page_locators.SIXTH_QUESTION_ACTIVE,
                MainPageAnswerToQuestion.SIXTH_QUESTION_ANSWER,
            ),
            (
                main_page_locators.SEVENTH_QUESTION,
                main_page_locators.SEVENTH_QUESTION_ACTIVE,
                MainPageAnswerToQuestion.SEVENTH_QUESTION_ANSWER,
            ),
            (
                main_page_locators.EIGHTH_QUESTION,
                main_page_locators.EIGHTH_QUESTION_ACTIVE,
                MainPageAnswerToQuestion.EIGTH_QUESTION_ANSWER,
            ),
        ],
    )
    def test_questions_drop_down_list(self, driver, question, answer, true_answer):
        question_main_page = QuestionsAboutTheImportant(self)
        question_main_page.scroll(driver)
        question_main_page.wait_clickable_element(driver, question)
        question_main_page.click_on_question(driver, question)
        assert question_main_page.answer_text(driver, answer) == true_answer


class TestNavigationOnSite:
    @allure.title("Проверяем попадание на главную страницу, нажав лого Самокат")
    def test_go_to_main_page_click_scooter_logo(self, driver):
        navigation = NavigationOnSite(self)
        navigation.click_order_button(driver)
        navigation.click_logo_scooter(driver)
        assert navigation.get_current_url(driver) == Urls.QA_SCOOTER

    @allure.title("Проверяем редирект на страницу Дзена")
    def test_click_yandex_logo_redirect_on_dzen(self, driver):
        navigation = NavigationOnSite(self)
        navigation.click_yandex_logo(driver)
        navigation.switch_on_tab(driver)
        navigation.wait_clickable_element(driver, main_page_locators.DZEN_SEARCH_BUTTON)
        assert navigation.get_current_url(driver) == Urls.REDIRECT_DZEN
