import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@allure.feature("UI Tests")
@pytest.mark.ui
class TestUI:

    @allure.story("Поиск билетов")
    def test_search_tickets(self, browser):
        with allure.step("Открыть сайт"):
            browser.get("https://www.aviasales.ru/")
        with allure.step("Проверить наличие поля поиска"):
            assert browser.find_element(By.NAME, "origin")

    @allure.story("Покупка билета")
    def test_buy_ticket(self, browser):
        with allure.step("Открыть сайт"):
            browser.get("https://www.aviasales.ru/")
        with allure.step("Проверить наличие кнопки поиска"):
            assert browser.find_element(By.CLASS_NAME, "search-button")

    @allure.story("Выбор обратного перелета")
    def test_round_trip_ticket(self, browser):
        with allure.step("Открыть сайт"):
            browser.get("https://www.aviasales.ru/")
        with allure.step("Проверить наличие чекбокса обратного билета"):
            assert browser.find_element(By.NAME, "return_date")

    @allure.story("Фильтрация по количеству пассажиров")
    def test_passengers_filter(self, browser):
        with allure.step("Открыть сайт"):
            browser.get("https://www.aviasales.ru/")
        with allure.step("Открыть фильтр пассажиров"):
            assert browser.find_element(By.CLASS_NAME, "passengers-field")

    @allure.story("Дополнительная фильтрация")
    def test_additional_filter(self, browser):
        with allure.step("Открыть сайт"):
            browser.get("https://www.aviasales.ru/")
        with allure.step("Проверить наличие фильтров"):
            assert browser.find_element(By.CLASS_NAME, "filters")
