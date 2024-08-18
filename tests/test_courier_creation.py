import allure
import requests
from test_data import *

class TestCourierCreation:

    @allure.title('Проверки: 1.Курьера можно создать 2.Чтобы создать курьера, нужно передать в ручку все обязательные поля 3.запрос возвращает правильный код ответа 4.успешный запрос возвращает правильное тело')
    def test_create_courier(self):
        payload = {
            "login": "Tester2049",
            "password": "123456",
            "firstName": "Courierb2"
        }

        response = requests.post(COURIER_CREATION_URL, json=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Проверка, если одного из полей нет, запрос возвращает ошибку')
    def test_create_courier_missing_password_field(self):
        payload = {
            "login": "Tester18922",
            "firstName": "Courierb2"
        }

        response = requests.post(COURIER_CREATION_URL, json=payload)

        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers(self):
        payload = {
            "login": "Tester583",
            "password": "123456",
            "firstName": "Courierb2"
        }

        r = requests.post(COURIER_CREATION_URL, json=payload)
        assert r.status_code == 201
        assert r.json() == {"ok": True}
        re = requests.post(COURIER_CREATION_URL, json=payload)
        assert re.status_code == 409
        assert re.json() == {"code": 409,"message": "Этот логин уже используется. Попробуйте другой."}

    @allure.title('Проверка, если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_create_courier_with_repeating_login(self):
        payload = {
            "login": "Tester1",
            "password": "123456",
            "firstName": "Courierb2"
        }

        re = requests.post(COURIER_CREATION_URL, json=payload)
        assert re.status_code == 409
        assert re.json() == {"code": 409,"message": "Этот логин уже используется. Попробуйте другой."}


