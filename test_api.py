import pytest
import requests
import allure
import os

BASE_URL = "https://auth.avs.io/api/user/settings"
TOKEN = os.getenv("API_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

@allure.feature("API Tests")
@pytest.mark.api
class TestAPI:

    @allure.story("Смена карты оплаты")
    def test_change_payment_card(self):
        payload = {"payment_options": ["ru_card"]}
        response = requests.patch(BASE_URL, json=payload, headers=headers)
        assert response.status_code == 200

    @allure.story("Смена имени профиля")
    def test_change_profile_name(self):
        payload = {"name": "Ксения"}
        response = requests.patch(BASE_URL, json=payload, headers=headers)
        assert response.status_code == 200

    @allure.story("Добавление email")
    def test_add_email(self):
        payload = {"email": "test@example.com"}
        response = requests.patch(BASE_URL, json=payload, headers=headers)
        assert response.status_code == 200

    @allure.story("Добавление пустого email (негативный тест)")
    def test_add_empty_email(self):
        payload = {"email": ""}
        response = requests.patch(BASE_URL, json=payload, headers=headers)
        assert response.status_code == 400

    @allure.story("Добавление некорректной страны проживания")
    def test_add_invalid_country(self):
        payload = {"market": "INVALID"}
        response = requests.patch(BASE_URL, json=payload, headers=headers)
        assert response.status_code == 400
